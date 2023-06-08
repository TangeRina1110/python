import math
def main(y, z, x):
    sum = 0
    n=len(y)
    for i in range(1, n+1):
        sum += pow((x[n+1- math.ceil(i/4)-1]+ 59 * pow(z[n+1-math.ceil(i/3)-1],3) + 61*pow(y[n+1 -math.ceil(i/3)-1],2)),4)
    return sum

print(main([-0.8, -0.3, -0.25, -0.41, 0.33, 0.63, 0.48],
[0.02, 0.38, -0.56, 0.42, -0.62, 0.7, 0.37],
[-0.99, 0.38, 0.11, 0.27, 0.04, -0.13, 0.46]))
