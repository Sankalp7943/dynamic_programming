#tabulation

x = "acbcf"
y = "abcdaf"

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

print(dp[n][m])
for i in dp:
    print(i)

ans=""
while not(n==0 and m==0):
    if x[m-1]==y[n-1]:
        ans+=x[m-1]
        m-=1
        n-=1
    else:
        if dp[n][m-1]>dp[n-1][m]:   #equality point taken care of
            ans+=x[m-1]
            m-=1
        else:
            ans+=y[n-1]
            n-=1
if not (n==0 and m==0):
    if n:
        ans = y[0:n-1]+ans[::-1]
    else:
        ans = x[0:m-1]+ans[::-1]
print(ans[::-1])


