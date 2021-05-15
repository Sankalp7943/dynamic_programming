
x = "abcdgh"
y = "abedfhr"
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
                dp[n][m] = 0 #because continuity is required

# for ans print(max of dp )
ans = 0
for i in dp:
    ans = max(ans, max(i))

print(ans)

