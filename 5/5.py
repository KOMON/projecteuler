import math

def gcd(x,y):
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y

def lcm(x,y):
    return (x*y)/gcd(x,y)

num = 1
for x in range(2, 21):
    num = lcm(num,x)

print num 
