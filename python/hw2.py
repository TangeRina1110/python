import math


def main(z):
    if z < 122:
        return 78*math.sin(z)**6 - 58*(z**2/65 + z)
    elif 167 >= z >=122:
        return z**5/78
    elif 235 > z >= 167:
        return math.log(z**2 - 92 - z/8)**6 - z - (z**3 - z**2)**2
    else:
        return math.atan(z**3/80) - z**4 - z**7
    
print(main(229))
