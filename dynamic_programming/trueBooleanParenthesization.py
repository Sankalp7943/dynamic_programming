#recursive

string = "T&F^T|F&F|T"
# ((T&F)^(T|F))&(F|T)
# F ^ T & T
# T

def solve(string, i, j, isTrue):
    if i>j:
        return 0
    if i==j:
        if isTrue:
            if string[i]=="T":
                return 1
            else:
                return 0
        else:
            if string[i]=="F":
                return 1
            else:
                return 0
    ans = 0
    for k in range(i+1, j, 2):  #i+1 to j-1, increment by 2 to always come on an operator
        leftTrue = solve(string, i, k-1, True)
        leftFalse = solve(string, i, k-1, False)
        rightTrue = solve(string, k+1, j, True)
        rightFalse = solve(string, k+1, j, False)
        if string[k]=="&":
            if isTrue:
                ans = ans + (leftTrue * rightTrue)
            else:
                ans = ans + (leftTrue * rightFalse) + (leftFalse * rightFalse) + (leftFalse * rightTrue)
        elif string[k]=="|":
            if isTrue:
                ans = ans + (leftTrue * rightFalse) + (leftFalse * rightTrue) + (leftTrue * rightTrue)
            else:
                ans = ans + (leftFalse * rightFalse)
        elif string[k]=="^":
            if isTrue:
                ans = ans + (leftFalse * rightTrue) + (leftTrue * rightFalse)
            else:
                ans = ans + (leftTrue * rightTrue) + (leftFalse * rightFalse)
        else:
            raise ("Stupid program")
    return ans

print(solve(string, 0 , len(string)-1, True))