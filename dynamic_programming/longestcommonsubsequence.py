#recursion

x = "abcdgh"
y = "abedfhr"
#expected = len(abdh) => 4
# subsequence can have pauses(discontinuity) just have to be in a flow. substring is continous
#base condition, choice diagram, ip smaller for next call

m = len(x)
n = len(y)

def lcs_recursion(x,y,m,n):
    if m==0 or n==0:
        return 0
    else:
        if x[m-1]== y[n-1]:
            return (1+lcs_recursion(x,y,m-1,n-1))
        else:
            return max(lcs_recursion(x,y,m-1,n), lcs_recursion(x,y,m,n-1))

print(lcs_recursion(x,y,m,n))

#memoize (array only has the stuff already calculated for, final array is not always a complete dp table)
dp = [[-1 for col in range(m+1)] for row in range(n+1)]

def lcs_memoize(x,y,m,n):
    if dp[n][m]!= -1:
        return dp[n][m]
    if m==0 or n==0:
        dp[n][m] = 0
        return dp[n][m]
    else:
        if x[m-1]== y[n-1]:
            dp[n][m] = (1+lcs_memoize(x,y,m-1,n-1))
            return dp[n][m]
        else:
            dp[n][m] = max(lcs_memoize(x,y,m-1,n), lcs_memoize(x,y,m,n-1))
            return dp[n][m]

print(lcs_memoize(x,y,m,n))
# for i in dp:
#     print(i)

#tabulation
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
# for i in dp:
#     print(i)

    