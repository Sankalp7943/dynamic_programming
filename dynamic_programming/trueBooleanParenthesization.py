#recursive

string = "T&F^T|F&F|T"
# ((T&F)^(T|F))&(F|T)
# F ^ T & T
# T

def solve(string, i, j, isTrue):
    if i>j:
        return 0
    if i==j:
        if isTrue:
            if string[i]=="T":
                return 1
            else:
                return 0
        else:
            if string[i]=="F":
                return 1
            else:
                return 0
    ans = 0
    for k in range(i+1, j, 2):  #i+1 to j-1, increment by 2 to always come on an operator
        leftTrue = solve(string, i, k-1, True)
        leftFalse = solve(string, i, k-1, False)
        rightTrue = solve(string, k+1, j, True)
        rightFalse = solve(string, k+1, j, False)
        if string[k]=="&":
            if isTrue:
                ans = ans + (leftTrue * rightTrue)
            else:
                ans = ans + (leftTrue * rightFalse) + (leftFalse * rightFalse) + (leftFalse * rightTrue)
        elif string[k]=="|":
            if isTrue:
                ans = ans + (leftTrue * rightFalse) + (leftFalse * rightTrue) + (leftTrue * rightTrue)
            else:
                ans = ans + (leftFalse * rightFalse)
        elif string[k]=="^":
            if isTrue:
                ans = ans + (leftFalse * rightTrue) + (leftTrue * rightFalse)
            else:
                ans = ans + (leftTrue * rightTrue) + (leftFalse * rightFalse)
        else:
            raise ("Stupid program")
    return ans

print(solve(string, 0 , len(string)-1, True))

# memoize
string = "T&F^T|F&F|T"
# ((T&F)^(T|F))&(F|T)
# F ^ T & T
# T

def dpsolve(string, i, j, isTrue):
    if isTrue:
        key = 0
    else:
        key = 1
    if dp[key][i][j]!=-1:
        return dp[key][i][j]
    if i>j:
        dp[key][i][j] = 0
        return dp[key][i][j]
    if i==j:
        if isTrue:
            if string[i]=="T":
                dp[key][i][j] = 1
                return dp[key][i][j]
            else:
                dp[key][i][j] = 0
                return dp[key][i][j]
        else:
            if string[i]=="F":
                dp[key][i][j] = 1
                return dp[key][i][j]
            else:
                dp[key][i][j] = 0
                return dp[key][i][j]
    ans = 0
    for k in range(i+1, j, 2):  #i+1 to j-1, increment by 2 to always come on an operator
        leftTrue = dp[0][i][k-1] if dp[0][i][k-1]!=-1 else dpsolve(string, i, k-1, True)
        leftFalse = dp[1][i][k-1] if dp[1][i][k-1]!=-1 else dpsolve(string, i, k-1, False)
        rightTrue = dp[0][k+1][j] if dp[0][k+1][j]!=-1 else dpsolve(string, k+1, j, True)
        rightFalse = dp[1][k+1][j] if dp[1][k+1][j]!=-1 else dpsolve(string, k+1, j, False)
        if string[k]=="&":
            if isTrue:
                ans = ans + (leftTrue * rightTrue)
            else:
                ans = ans + (leftTrue * rightFalse) + (leftFalse * rightFalse) + (leftFalse * rightTrue)
        elif string[k]=="|":
            if isTrue:
                ans = ans + (leftTrue * rightFalse) + (leftFalse * rightTrue) + (leftTrue * rightTrue)
            else:
                ans = ans + (leftFalse * rightFalse)
        elif string[k]=="^":
            if isTrue:
                ans = ans + (leftFalse * rightTrue) + (leftTrue * rightFalse)
            else:
                ans = ans + (leftTrue * rightTrue) + (leftFalse * rightFalse)
        else:
            raise ("Stupid program")
    dp[key][i][j] = ans
    return dp[key][i][j]

dp = [[[-1 for i in range(len(string)+1)] for j in range(len(string)+1)]for k in range(2)]

print(dpsolve(string, 0 , len(string)-1, True))
for i in dp:
    for j in i:
        print(j)
    print("\n")