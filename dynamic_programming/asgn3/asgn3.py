from dataclasses import dataclass
import unittest

@dataclass
class GeneAlignment:
    delta: dict[str, dict[str, int]]
    def best_alignment(self, x: str, y: str) -> tuple:
        n = len(x)
        m = len(y)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            


class TestGeneAlignment(unittest.TestCase):

    def setUp(self):
        scoring_matrix = {
            'A': {'A': 2,  'C': -1, 'G': -1, 'T': -1, '-': -2},
            'C': {'A': -1, 'C': 2,  'G': -1, 'T': -1, '-': -2},
            'G': {'A': -1, 'C': -1, 'G': 2,  'T': -1, '-': -2},
            'T': {'A': -1, 'C': -1, 'G': -1, 'T': 2,  '-': -2},
            '-': {'A': -2, 'C': -1, 'G': -2, 'T': -2, '-': 0}}
        self.genes = GeneAlignment(scoring_matrix)
        

    def test_example(self):
        x = "ATGCC"
        y = "TACGCA"
        expected_score = 2
        expected_x = "-ATGCC"
        expected_y = "TACGCA"
        result = self.genes.best_alignment(x, y)
        self.assertEqual(result, (expected_score, expected_x, expected_y))

if __name__ == "__main__":
    unittest.main()