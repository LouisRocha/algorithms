from dataclasses import dataclass
import unittest

@dataclass
class GeneAlignment:
    delta: dict[str, dict[str, int]]
    def best_alignment(self, x: str, y: str) -> tuple:
        #init. matrix
        n = len(x)
        m = len(y)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        #base
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + self.delta[x[i - 1]]["-"]
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + self.delta["-"][y[j - 1]]
        
        #fill table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                no_gap = dp[i - 1][j - 1] + self.delta[x[i - 1]][y[j - 1]]
                gap_x = dp[i - 1][j] + self.delta[x[i - 1]]['-']
                gap_y = dp[i][j - 1] + self.delta['-'][y[j - 1]]
                dp[i][j] = max(no_gap, gap_x, gap_y)
        
        # reconstruct alignment
        expected_x = []
        expected_y = []
        i = n
        j = m
        while (i > 0) or (j > 0):
            if (i > 0) and (j > 0) and (dp[i][j] == dp[i - 1][j - 1] + self.delta[x[i - 1]][y[j - 1]]):
                expected_x.append(x[i - 1])
                expected_y.append(y[j - 1])
                i -= 1
                j -= 1
            elif (i > 0) and (dp[i][j] == dp[i - 1][j] + self.delta[x[i - 1]]["-"]):
                expected_x.append(x[i - 1])
                expected_y.append("-")
                i -= 1
            else:
                expected_x.append("-")
                expected_y.append(y[j - 1])
                j -= 1

        expected_x = "".join(reversed(expected_x))
        expected_y = "".join(reversed(expected_y))

        # Visualizer
        # for row in dp:
        #     print(row)

        return (dp[n][m], expected_x, expected_y)

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