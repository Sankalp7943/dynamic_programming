# recursion

def knapsack(capacity, weight, value, n):
    if n == 0 or capacity == 0: #base condition
        return 0
    if weight[n-1] <= capacity:
        return max((value[n-1] + knapsack(capacity-weight[n-1],weight,value,n-1)),knapsack(capacity,weight,value,n-1))
    else:
        return knapsack(capacity,weight,value,n-1)

capacity = 100
weight = [10, 20, 30, 10, 20 , 25]
value = [10, 30, 40, 100, 26, 15]
n = len(weight)

ans = knapsack(capacity, weight, value, n)
print(ans)

    