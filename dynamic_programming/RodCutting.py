def CutRod(prices: list[int], n: int) -> int:
    #init. cache
    revenue = [-1] * (n + 1)

    #basecase
    revenue[0] = 0

    #recurrence
    for i in range(1, n + 1):
        current = -1
        for j in range(1, i + 1):
            current = max(current, prices[j - 1] + revenue[i - j])
        revenue[i] = current
    return revenue [n]

inches = 4
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(CutRod(prices, inches))