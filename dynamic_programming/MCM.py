#recursion
arr = [40, 20, 30, 10 ,30]  # A(i) = arr[i-1]*arr[i]

def solve(arr, i, j):
    if i >= j:
        return 0
    ans = float('inf')
    for k in range(i,j,1):  #i to j-1
        tempans = solve(arr, i, k)+ solve(arr, k+1, j)+ (arr[i-1]*arr[k]*arr[j])
        ans = min(ans, tempans)
    return ans

print(solve(arr, 1, len(arr)-1)) #i should be in from 1 as arr[i-1] is taken too. and j can be at last index

