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