import math
def main (b, a, n, y):
    sum = 0
    for j in range(1, n+1):
        for c in range(1, a+1):
            for k in range(1, b+1):
                sum += (((y**2/14 - j - c**3)**5)/57 - k**4 -
                        66*math.exp(y)**3)
    return sum
print(main(5, 4, 2, 0.17))
