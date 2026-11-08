import math
import unittest

from scipy import stats

from src.mann_whitney import mann_whitney_test, pooled_ranks, rank_summary
from src.welch_test import welch_test


class PooledRankTests(unittest.TestCase):
    def test_ascending_ranks_preserve_observation_ids(self):
        rows = pooled_ranks([30, 10], [20, 40])
        self.assertEqual(
            [(row["latency_ms"], row["group"], row["observation_id"], row["rank"])
             for row in rows],
            [(10, "A", 2, 1), (20, "B", 1, 2), (30, "A", 1, 3), (40, "B", 2, 4)],
        )
        self.assertEqual(rank_summary(rows), {"rank_sum_a": 4, "rank_sum_b": 6, "tie_count": 0})

    def test_ties_across_groups_and_within_group(self):
        rows = pooled_ranks([4, 1, 4], [1, 2])
        self.assertEqual([row["rank"] for row in rows], [1.5, 1.5, 3, 4.5, 4.5])
        self.assertEqual([row["tie_size"] for row in rows], [2, 2, 1, 2, 2])
        summary = rank_summary(rows)
        self.assertEqual(summary, {"rank_sum_a": 10.5, "rank_sum_b": 4.5, "tie_count": 2})
        self.assertEqual(summary["rank_sum_a"] + summary["rank_sum_b"], 5 * 6 / 2)

    def test_invalid_samples(self):
        for sample in ([], [[1, 2]], [float("nan")]):
            with self.subTest(sample=sample), self.assertRaises(ValueError):
                pooled_ranks(sample, [1, 2])


class MannWhitneyTests(unittest.TestCase):
    def test_separated_samples_and_continuity_correction(self):
        a, b = [1, 2, 3], [4, 5, 6]
        result = mann_whitney_test(a, b, 0.05)
        z = 4 / math.sqrt(5.25)
        self.assertEqual((result["u_a"], result["u_b"]), (0, 9))
        self.assertEqual(result["variance_u"], 5.25)
        self.assertAlmostEqual(result["z"], z)
        self.assertAlmostEqual(result["p_value"], 2 * stats.norm.sf(z))
        self.assertAlmostEqual(result["p_value_scipy"], result["p_value"])
        self.assertTrue(mann_whitney_test(a, b, result["p_value"])["reject_h0"])
        self.assertAlmostEqual(mann_whitney_test(b, a, 0.05)["p_value"], result["p_value"])

    def test_midrank_variance_for_ties(self):
        result = mann_whitney_test([4, 1, 4], [1, 2], 0.05)
        self.assertEqual((result["u_a"], result["u_b"]), (4.5, 1.5))
        self.assertEqual((result["pair_a_greater"], result["pair_b_greater"], result["pair_equal"]),
                         (4, 1, 1))
        self.assertAlmostEqual(result["variance_u"], 2.7)
        self.assertAlmostEqual(result["z"], 1 / math.sqrt(2.7))
        self.assertAlmostEqual(result["p_value_scipy"], result["p_value"])

    def test_central_and_all_tied_cases(self):
        central = mann_whitney_test([1, 4], [2, 3], 0.05)
        self.assertEqual((central["u_min"], central["u_max"]), (2, 2))
        self.assertEqual(central["p_value"], 1)
        all_tied = mann_whitney_test([1, 1], [1, 1], 0.05)
        self.assertEqual(all_tied["variance_u"], 0)
        self.assertIsNone(all_tied["z"])
        self.assertEqual(all_tied["p_value"], 1)
        self.assertFalse(all_tied["reject_h0"])


class WelchTests(unittest.TestCase):
    def test_statistic_and_df_from_hand_calculation(self):
        a, b = [1, 2, 3], [1, 5, 9, 13]
        result = welch_test(a, b, 0.05)
        self.assertAlmostEqual(result["mean_difference_ms"], -5)
        self.assertAlmostEqual(result["standard_error_ms"], math.sqrt(7))
        self.assertAlmostEqual(result["t"], -5 / math.sqrt(7))
        self.assertAlmostEqual(result["df"], 2646 / 803)
        self.assertEqual(result["df_course"], 3)
        self.assertAlmostEqual(result["p_value"], 2 * stats.t.sf(5 / math.sqrt(7), 3))
        self.assertAlmostEqual(result["p_value_scipy"], 2 * stats.t.sf(5 / math.sqrt(7), 2646 / 803))
        self.assertFalse(result["reject_h0"])
        self.assertFalse(welch_test(a, b, result["p_value"])["reject_h0"])

    def test_sign_changes_and_p_value_is_two_sided(self):
        a, b = [1, 2, 3, 4], [20, 21, 22, 23]
        forward = welch_test(a, b, 0.05)
        backward = welch_test(b, a, 0.05)
        self.assertAlmostEqual(forward["t"], -backward["t"])
        self.assertAlmostEqual(forward["p_value"], backward["p_value"])
        self.assertTrue(forward["reject_h0"])

    def test_invalid_inputs(self):
        for a, b, alpha in (([1], [2, 3], 0.05), ([1, 1], [2, 2], 0.05),
                            ([1, 2], [2, 3], 1), ([1, 2], [2, float("inf")], 0.05)):
            with self.subTest(a=a, b=b, alpha=alpha), self.assertRaises(ValueError):
                welch_test(a, b, alpha)


if __name__ == "__main__":
    unittest.main()
