'''def main(x, y, z): #Var1
    sum = 0
    n = len(x)
    x = [0] + x
    y = [0] + y
    z = [0] + z
    for i in range(1, n+1):
        a = y[n+1-i]**2 + (x[i]**3)/46
        b = 82*z[n+1-i]
        sum += 44*(a+b)**7
    return 89*sum

print(main([0.57, -0.98, -0.17, 0.16, -0.37, 0.25, -0.04],
[-0.43, -0.34, -0.34, -0.44, 0.35, 0.27, 0.24],
[-0.86, -0.41, -0.89, -0.65, 0.01, -0.5, -0.7]))'''

'''def main(y, z):
    sum = 0
    n = len(y)
    y = [0] + y
    z = [0] + z
    for i in range(1, n + 1):
        sum += 81 * (54 * y[n+1-i] - z[n + 1 - i] ** 3 - 16 * z[n + 1 - i] ** 2) ** 3
    return sum

print(main([0.08, 0.67, 0.7, -0.44],
[0.2, -0.58, -0.18, 0.74]))'''


'''import math
def main(x, y, z):
    sum = 0
    n = len(x)
    x = [0] + x
    y = [0] + y
    z = [0] + z
    for i in range(1, n +1):
        sum += ((x[math.ceil(i/2)]**2 - 74 * z[n+1-i] - 38*y[i]**3)**6)/ 82

    return sum

print(main([0.34, 0.5],
[0.97, -0.12],
[0.88, 0.72]))'''

'''def main(x, y):
    sum = 0
    n = len(x)
    x = [0]+x
    y = [0]+y
    for i in range(1, n+1):
        sum += ((95*x[n+1-i]**2 - 49*y[i]**3 -1)**5)/36
    return sum
print(main([0.87, -0.62, -0.71, -0.85, -0.37, -0.47],
[-0.82, -0.07, -0.3, -0.56, -0.03, 0.13]))'''

'''import math
def main(y, z, x):
    sum = 0
    n = len(y)
    x = [0]+x
    y = [0]+y
    z = [0]+z
    for i in range(1, n+1):
        a = x[n + 1-math.ceil(i/4)]
        b = (z[n+1-math.ceil(i/3)])**3
        c = (y[n+1-math.ceil(i/3)])**2
        sum += (a+59*b+61*c)**4
    return sum

print(main([0.01, 0.08, 0.58, -0.34, 0.65],
[0.31, 0.51, -0.51, -0.35, -0.31],
[-0.94, -0.58, -0.45, 0.17, -0.7]))'''

'''import math
def main(y):
    sum =0
    n = len(y)
    y = [0]+y
    for i in range(1, n+1):
        a = 49*y[n+1-i]**3 + 30*y[n+1-i]
        sum+= math.atan(a)**5
    return sum

print(main([-0.72, 0.88, -0.45, 0.36, 0.43]))'''

'''import math
def main(y, z, x):
    sum = 0
    n = len(y)
    y = [0] + y
    z= [0] +z
    x= [0] +x
    for i in range(1, n+1):
        a = 96*y[i]**3
        b= x[n+1-i]/81
        c = 44*z[math.ceil(i/2)]**2
        sum += math.tan(a - b - c)**5
    return sum

print(main([0.05, -0.13, 0.47, -0.15, 0.02, 0.85, -0.93],
[0.92, -0.04, 0.73, -0.3, -0.15, -0.96, 0.38],
[0.96, 0.78, -0.4, 0.98, 0.23, 0.11, 0.82]))'''

'''import math #var16
def main(x, y, z):
    sum =0
    n = len(x)
    x = [0]+x
    y = [0]+y
    z = [0]+z
    
    for i in range(1, n+1):
        a = x[i]**2/41
        b = y[i]**3/29
        c = 21*z[n+1-math.ceil(i/4)]
        sum+=(a+b+c)**6
    return 59*sum
print(main([0.92, -0.56, 0.64, -1.0, 0.34],
[-0.22, 0.88, 0.09, 0.81, 0.55],
[-0.16, -0.02, 0.33, -0.11, -0.82]))'''

'''#var23
import math
def main(y, x, z):
    sum = 0
    n = len(y)
    y = [0]+y
    x = [0]+x
    z = [0]+z
    for i in range(1, n+1):
        a = 49*x[math.ceil(i/3)]
        b = 65*z[n+1-math.ceil(i/2)]**3
        c = y[math.ceil(i/2)]**2
        sum += 52 * abs(a - b - c)
    return sum

print(main([-0.81, 0.41, 0.85, -0.41, 0.77, 0.25, 0.15],
[0.76, 0.23, -0.39, 0.15, -0.78, 0.17, 0.37],
[-0.03, -0.75, -0.56, -0.62, -0.47, 0.61, 0.59]))
print(main([0.33, -0.44, 0.29, 0.21, 0.07, -0.73, 0.82],
[-0.95, 0.03, -0.82, -0.35, 0.34, -0.22, -0.86],
[0.07, 0.62, -0.97, 0.34, 0.55, 0.73, -0.82]))
print(main([0.59, -0.0, -0.67, -0.23, -0.25, 0.3, -0.23],
[0.29, -0.97, 0.87, 0.67, 0.91, 0.4, 0.05],
[0.68, 0.72, -0.19, -0.76, 0.49, -0.98, -0.95]))
print(main([-0.07, 0.0, -0.8, -0.24, -0.7, -0.78, 0.27],
[-0.74, 0.89, 0.29, -0.56, -0.3, -0.83, 0.29],
[-0.13, -0.59, 0.96, 0.26, -0.29, -0.65, -0.62]))
print(main([-0.22, -0.76, 0.94, -0.91, 0.07, 0.95, 0.41],
[-0.63, 0.72, 0.22, -0.09, 0.87, 0.47, 0.69],
[-0.58, -0.93, -0.64, -0.1, 0.43, -0.24, 0.65]))'''

'''import math #var40
def main(y):
    sum = 0
    n = len(y)
    y = [0]+y
    for i in range(1, n + 1):
        a = 20*y[i]**3
        b = y[n+1-i]
        c = 84 * y[n+1-i]**2
        sum += 86 * math.sin(a - b - c)**5
    return sum
print(main([-0.15, 0.64, 0.52, -0.02, -0.28]))
print(main([-0.34, -0.09, -0.14, 0.22, 0.91]))
print(main([-0.2, 0.13, -0.88, -0.9, -0.93]))
print(main([-0.25, -0.87, -1.0, -0.31, 0.42]))
print(main([1.0, 0.18, -0.92, 0.45, 0.76]))'''

import math


'''def main(z, y, x):
    sum = 0
    n = len(z)
    x = [0] + x
    y = [0] + y
    z = [0] + z
    for i in range(1, n+1):
        a = 55*y[n+1-i]**3
        b = x[n+1-i]**2
        c = z[n+1-i]
        sum += 80*math.floor(a - b - c)**7
    return 45*sum

print(main([0.02, 0.18, -0.92],
[0.89, 0.1, 0.09],
[0.97, 0.43, -0.97]))
print(main([-0.0, -0.99, -0.56],
[-0.71, 0.54, -0.89],
[0.78, 0.94, 0.59]))
print(main([0.85, 0.37, -0.94],
[0.57, -0.33, 0.8],
[-0.99, 0.22, -0.99]))
print(main([-0.64, 0.44, -0.58],
[0.32, -0.46, -0.96],
[0.89, -0.29, -0.77]))
print(main([-0.2, -0.04, 0.75],
[-0.88, 0.31, 0.31],
[0.96, 0.74, 0.57]))  '''

а е
