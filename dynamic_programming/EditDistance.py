def EditDistance(w1, w2):
    n = len(w1)
    m = len(w2)

    # creating the grid map thingy
    map = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        map[i][0] = i
    for j in range(m + 1):
        map[0][j] = j

    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if w1[i - 1] == w2[j - 1]:
                map[i][j] = map[i - 1][j - 1]
            else:
                map[i][j] = 1 + min(map[i - 1][j - 1],
                                    map[i][j - 1],
                                    map[i - 1][j])

    # not part of algorithm but shows grid
    for picture in map:
        print(picture)

    return map[n][m]

print(EditDistance("cat", "cut"))