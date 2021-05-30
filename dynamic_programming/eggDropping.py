#e = eggs
#f = floors
def solve(e, f):
    if e == 1:
        return f
    if f<=1:
        return f
    attempts = float("inf")
    for k in range(1,f+1):
        temp = 1+max(solve(e-1,k-1), solve(e, f-k)) #max due to worst case
        attempts = min(attempts, temp)
    return attempts
print(solve(2,10))