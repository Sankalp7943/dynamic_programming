#e = eggs
#f = floors
def solve(e, f):
    if e == 1:
        return f
    if f<=1:
        return f
    attempts = float("inf")
    for k in range(1,f+1):
        temp = 1+max(solve(e-1,k-1), solve(e, f-k)) #max due to worst case
        attempts = min(attempts, temp)
    return attempts
print(solve(2,10))


#dp
e = 20
f = 100
dp = [[-1 for i in range(e+1)] for j in range(f+1)]

def solvedp(e, f):
    if dp[f][e]!=-1:
        return dp[f][e]
    if e == 1:
        dp[f][e] = f
        return dp[f][e]
    if f<=1:
        dp[f][e] = f
        return dp[f][e]
    attempts = float("inf")
    for k in range(1,f+1):
        egg_broke = solvedp(e-1,k-1)
        egg_not_break = solvedp(e, f-k)
        temp = 1+max(egg_broke, egg_not_break) #max due to worst case
        attempts = min(attempts, temp)
    dp[f][e] = attempts
    return dp[f][e]
print(solvedp(e,f))
# for i in dp:
#     print(i)