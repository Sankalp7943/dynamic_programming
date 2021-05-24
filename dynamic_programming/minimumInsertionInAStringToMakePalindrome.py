x = "aebcbda"
y = x[::-1]

m = len(x)
n = len(y)
dp = [[-1 for col in range(m+1)] for row in range(n+1)]

rows = n+1
cols = m+1
for n in range(rows):
    for m in range(cols):
        if n==0 or m==0:
            dp[n][m] = 0
        else:
            if x[m-1]==y[n-1]:
                dp[n][m] = 1+ dp[n-1][m-1]
            else:
                dp[n][m] = max(dp[n-1][m],dp[n][m-1])

print("Minimum insertions: ", len(x)-dp[n][m]) # same like deletion