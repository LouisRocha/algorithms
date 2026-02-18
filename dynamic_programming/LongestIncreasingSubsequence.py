def LIS(A, n):
    if n == 0:
        return 0
    m = 1
    for i in range(n):
        if A[i] < A[n]:
            m = max(m, 1 + LIS(A, i))

    return m

A = [5, 2, 8, 6, 3, 6, 9, 7]
n = len(A)

print(LIS(A, n - 1))