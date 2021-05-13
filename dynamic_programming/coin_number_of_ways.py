#tabulation direct
"""
unbounded knapsack with similarity to target sum subset problem
"""

coins = [1,2,3]
target = 5
n = len(coins)

dp = [[-1 for i in range(target+1)] for j in range(n+1)]    #array initialise


for i in range(n+1):
    dp[i][0] =1
for i in range(target+1):
    dp[0][i]=0


for n in range(1,len(coins)+1):
    for amount in range(1,target+1):
        if coins[n-1]>amount:
            dp[n][amount]=dp[n-1][amount]
        else:
            dp[n][amount] = dp[n][amount-coins[n-1]] + dp[n-1][amount]
target = 5
n = len(coins)
print(dp[n][target])
for i in dp:
    print(i)