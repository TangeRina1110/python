import math
def main(x, y, z):
    a = 47*(76*z + 46 + 77*y**2)**4 + math.asin(x**2/13 + z**3)**2
    b = 5 *(math.log10(y)**7) - 85*(15*x**3 - z**2 - 1)**5
    с = math.log(y)**2/9 - 76*(z**3 - x)**3
    return a/b - c
print(main(0.41, -0.24, 0.48))
