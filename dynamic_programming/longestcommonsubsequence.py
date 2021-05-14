#recursion

x = "abcdgh"
y = "abedfhr"
#expected = len(abdh) => 4
# subsequence can have pauses(discontinuity) just have to be in a flow. substring is continous
#base condition, choice diagram, ip smaller for next call

m = len(x)
n = len(y)

def lcs_recursion(x,y,m,n):
    if m==0 or n==0:
        return 0
    else:
        if x[m-1]== y[n-1]:
            return (1+lcs_recursion(x,y,m-1,n-1))
        else:
            return max(lcs_recursion(x,y,m-1,n), lcs_recursion(x,y,m,n-1))

print(lcs_recursion(x,y,m,n))
    
    