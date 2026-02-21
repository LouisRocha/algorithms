
x = 'ATGCC'
y = 'TACGCA'

n = len(x) #5
m = len(y) #6

dp = [[0] * (m + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    dp[i][0] = x[i - 1]
for j in range(1, m + 1):
    dp[0][j] = y[j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if x[i - 1] == y[j - 1]:
            dp[i][j] = 2
        else:
            dp[i][j] = 



for row in dp:
    print(row)