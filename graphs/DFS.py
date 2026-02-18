def Dfs(G):
    n = len(G)
    visited = [False] * n
    pre = [0] * n
    post = [0] * n
    clock = [1]

    for v in range(n):
        if not visited[v]:
            explore(G, v, visited, pre, post, clock)
    return pre, post

def explore(G, v, visited, pre, post, clock):

    visited[v] = True
    pre[v] = clock[0]
    clock[0] += 1

    for u in G[v]:
        if not visited[u]:
            explore(G, u, visited, pre, post, clock)

    post[v] = clock[0]
    clock[0] += 1


g1 = [
    [1, 2],
    [3],
    [],
    []
]

print(Dfs(g1))

