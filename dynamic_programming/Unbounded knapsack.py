# recursion

def unbounded_knapsack(capacity, weight, value, n):
    if n==0 or capacity==0:
        return 0
    if weight[n-1]>capacity:
        unbounded_knapsack(capacity, weight, value, n-1)
    else:
        return max(
            value[n-1]+unbounded_knapsack(capacity-weight[n-1],weight,value,n), unbounded_knapsack(capacity,weight,value,n-1)
        )

#memoized solution

def memoized_unbounded_knapsack(capacity, weight, value, n):
    if n == 0 or capacity == 0: #base condition
        dp[n][capacity] = 0
        return 0
    if dp[n][capacity] != -1:
        return dp[n][capacity]
    if weight[n-1] <= capacity:
        dp[n][capacity]= max((value[n-1] + memoized_unbounded_knapsack(capacity-weight[n-1],weight,value,n)),memoized_unbounded_knapsack(capacity,weight,value,n-1))
        return dp[n][capacity]
    else:
        dp[n][capacity]= memoized_unbounded_knapsack(capacity,weight,value,n-1)
        return dp[n][capacity]

capacity = 100
weight = [10, 20, 30, 10, 20 , 25]
value = [10, 30, 40, 100, 26, 15]
n = len(weight)
dp = [[-1]*(capacity+1)]*(n+1)


