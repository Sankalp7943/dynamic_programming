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

"""

