# """knapsack_1 = 0/1 knapsack (no repetition)"""
# """knapsack_2 = Unbounded knapsack (repetition)"""

def knapsack_1(weights: list[int], values: list[int], capacity: int) -> int:
    
    # Initialize Matrix -> n-items x capacity
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table
    for i in range(n + 1):
        for j in range (capacity + 1):
            
            # If there is no item or capacity is 0
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0

                # Pick ith item if it does not exceed the capacity
                if weights[i - 1] <= j:
                    pick = values[i - 1] + dp[i - 1][j - weights[i - 1]]

                # Don't pick the ith item
                notPick = dp[i - 1][j]
                dp[i][j] = max(pick, notPick)

    return dp[n][capacity]



def knapsack_2():
    return


tests = [
    ([1,2,3], [6,10,12], 5, 22),
    ([2,3,4], [4,5,6], 5, 9),
    ([5], [100], 5, 100),
    ([6], [100], 5, 0),
    ([], [], 10, 0),
    ([1,2,3], [10,20,30], 0, 0),
    ([10,20,30], [100,200,300], 5, 0),
    ([10,20,30], [60,100,120], 50, 220),
    ([1,2,2], [10,15,15], 3, 25),
    ([3,4,5,6], [2,3,4,1], 8, 6),
    ([4,2,3], [10,4,7], 6, 14),
]

for w, v, c, expected in tests:
    result = knapsack_1(w, v, c)
    print(result, "✓" if result == expected else f"✗ (expected {expected})")
