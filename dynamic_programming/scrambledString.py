# recursive

a = "great"
b = "ategr"
import sys
x=15000
sys.setrecursionlimit(x)

def isScramble(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    n = len(s1)
    if not n:
        return True   
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    for i in range(1, n):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])):
            return True
        if (isScramble(s1[-i:], s2[:i]) and isScramble(s1[:-i], s2[i:])):
            return True
    return False

print(isScramble(a,b))

#memoize
dic={}
a = "great"
b = "ategr"
def isScrambleDP(s1: str, s2: str) -> bool:
    if (s1, s2) in dic :
        return dic[(s1, s2)]
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        dic[(s1, s2)] = False     
        return False
    n = len(s1)
    if s1 == s2:
        dic[(s1, s2)] = True
        return True
    for i in range(1, n):
        if (isScrambleDP(s1[i:], s2[i:]) and isScrambleDP(s1[:i], s2[:i])):
            return True
        if (isScrambleDP(s1[:-i], s2[i:]) and isScrambleDP(s1[-i:], s2[:i])):
            return True
    dic[(s1, s2)] = False
    return False
print(isScrambleDP(a,b))