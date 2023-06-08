import math


def rec(n):
    if n == 0:
        return 0.12
    elif n == 1:
        return -0.97
    else:
        return math.tan(rec(n-2)) + math.atan(2*rec(n-1)**2)**3
       
print(rec(6))
    
