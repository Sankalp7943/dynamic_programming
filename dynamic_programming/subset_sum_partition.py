#recursion

def subset_sum(arr, target, n):
    if target == 0:
        return True
    if len(arr) == 0 or n == 0:
        return False
    if arr[n-1]>target:
        return subset_sum(arr, target, n-1)
    else:
        return subset_sum(arr, target-arr[n-1], n-1) or subset_sum(arr, target, n-1)


arr = [2,3,7,8,10]
target = 11
n = len(arr)
print(subset_sum(arr, target, n))


#dynamic programming varying factors are n and sum

def subset_sum_dp(arr, target, n):
    if dp[n][target] != -1:
        return dp[n][target]
    if target == 0:
        dp[n][target] = True 
        return dp[n][target]
    if len(arr) == 0 or n == 0:
        dp[n][target] = False
        return dp[n][target]
    if arr[n-1] > target:
        dp[n][target] = subset_sum_dp(arr, target, n-1)
        return dp[n][target]
    else:
        dp[n][target] = subset_sum_dp(arr, target-arr[n-1], n-1) or subset_sum_dp(arr, target, n-1)
        return dp[n][target]


arr = [2,3,7,8,10]
target = 20
n = len(arr)
dp = [[-1]*(target+1)]*(n+1)
print(subset_sum_dp(arr, target, n))