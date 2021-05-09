#dp
"""
this problem is same as subset_sum_partition
In this case target will be sum of arr divide by 2. If sum is odd, answer is false, if even then maybe.
"""

def equal_sum_partition_dp(arr, target, n):
    if dp[n][target] != -1:
        return dp[n][target]
    if target == 0:
        dp[n][target] = True 
        return dp[n][target]
    if len(arr) == 0 or n == 0:
        dp[n][target] = False
        return dp[n][target]
    if arr[n-1] > target:
        dp[n][target] = equal_sum_partition_dp(arr, target, n-1)
        return dp[n][target]
    else:
        dp[n][target] = equal_sum_partition_dp(arr, target-arr[n-1], n-1) or equal_sum_partition_dp(arr, target, n-1)
        return dp[n][target]

arr = [5, 1, 5, 11]
sum_arr = sum(arr)
n = len(arr)
if sum_arr%2:
    print("False")
else:
    target = sum_arr//2
    dp = [[-1]*(target+1)]*(n+1)
    ans = equal_sum_partition_dp(arr, target, n)
    print(ans)
