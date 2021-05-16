# to be solved using subset sum partition

#minimise range-2*S1
arr = [1,5,6,11]
n = len(arr)
sumRange = (0,sum(arr))
target = sumRange[1]

dp = [[-1 for i in range(target+1)]for j in range(n+1)]

for i in range(target+1):
    dp[0][i]= False

for i in range(n+1):
    dp[i][0]= True

for row in range(1,n+1):
    for col in range(1,target+1):
        if arr[row-1]>target:
            dp[row][col] = dp[row-1][col]
        else:
            dp[row][col] = dp[row-1][col] or dp[row-1][col-arr[row-1]]

for i in dp:
    print(i)
ans = float('inf')
for row in range(n+1):
    for col in range(target+1):
        if dp[row][col]:
            ans = min(ans,abs(target-(2*col)) )
print(ans)
            