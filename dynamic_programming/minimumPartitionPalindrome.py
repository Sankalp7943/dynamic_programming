#recursion
string = "nnitin"

def solve(string, i, j):
    if i >= j:
        return 0
    if string[i:j]==string[j:i:-1]:
        return 0
    ans = float('inf')
    for k in range(i,j,1):  #i to j-1
        tempans = solve(string, i, k)+ solve(string, k+1, j)+ 1
        ans = min(ans, tempans)
    return ans

print(solve(string, 0, len(string)-1))

#memoize


string = "nitik"
dp = [[-1 for i in range(len(string)+1)] for j in range(len(string)+1)]

def solve_dp(string, i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i >= j:
        dp[i][j] = 0
        return dp[i][j]
    if string[i:j]==string[j:i:-1]:
        dp[i][j] = 0
        return dp[i][j]
    ans = float('inf')
    for k in range(i,j,1):  #i to j-1
        tempans = solve_dp(string, i, k)+ solve_dp(string, k+1, j)+ 1
        ans = min(ans, tempans)
        dp[i][j] = ans
    return dp[i][j]

print(solve_dp(string, 0, len(string)-1))
for i in dp:
    print(i)

# further optimised

string = "nitik"
dp = [[-1 for i in range(len(string)+1)] for j in range(len(string)+1)]

def solve_dp2(string, i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i >= j:
        dp[i][j] = 0
        return dp[i][j]
    if string[i:j]==string[j:i:-1]:
        dp[i][j] = 0
        return dp[i][j]
    ans = float('inf')
    for k in range(i,j,1):  #i to j-1
        if dp[i][k]!= -1:
            left = dp[i][k]
        else:
            left = solve_dp2(string, i, k)
        if dp[k+1][j]!= -1:
            right = dp[k+1][j]
        else:
            right = solve_dp2(string, k+1, j)
        tempans = left + right + 1
        ans = min(ans, tempans)
        dp[i][j] = ans
    return dp[i][j]

print(solve_dp2(string, 0, len(string)-1))
for i in dp:
    print(i)