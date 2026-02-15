def knapsack_with_repetition(weights: list[int], values: list[int], w: int) -> int:
    map = createGrid(len(values), w)


    for row in map:
        print(row)
    return



def knapsack_without_repitition():
    return

#helper function
def createGrid(items, capacity) -> list[list[int]]:
    map = [[0] * (capacity + 1) for _ in range(items + 1)]
    for i in range(items + 1):
        map[i][0] = i
    for j in range(capacity + 1):
        map[0][j] = j
    return map

knapsack_with_repetition([7, 3, 4, 2], [4, 10, 5, 2], 9)