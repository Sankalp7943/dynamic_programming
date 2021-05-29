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