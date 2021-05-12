# recursion

def rod_cut(length, pieces, value, n):
    if n==0 or length==0:
        return 0
    if pieces[n-1]>length:
        return rod_cut(length, pieces, value, n-1)
    else:
        return max(value[n-1]+rod_cut(length-pieces[n-1],pieces,value,n), rod_cut(length,pieces,value,n-1))

length = 8
pieces = [1,2,3,4,5]
value = [2,4,7,3,8]
n = len(value)
ans = rod_cut(length, pieces, value, n)
print(ans)


#tabulation

"""
Only two attributes that varies are the length(length) and length of array(n)
Output is the max profit which will be the value stored in the table
"""

# dp = [[-1]*(length+1)]*(n+1)
rows, cols = (5, 5)
dp = [[-1 for i in range(length+1)] for j in range(n+1)]    #
# gives us a table with row as length and columns as different length of array


#initialise

for i in range(length+1):
    dp[0][i] = 0    #n=0 all rod length should give 0
for j in range(n+1):
    dp[j][0] = 0    #if length of rod is 0, profit will always be 0

for n in range(1,n+1):
    for length in range(1,length+1):
        if pieces[n-1] > length:
            dp[n][length] = dp[n-1][length]
        else:
            dp[n][length] = max(value[n-1]+dp[n][length-pieces[n-1]], dp[n-1][length])

ans = dp[n][length]
print (ans)
print("table of dp")
for i in dp:
    print(i)


