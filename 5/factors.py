import math

factors = []

SAMPLE = 2520


x = 1
while x <= SAMPLE:
    if (SAMPLE % x == 0):
        factors.append(x)
    x += 1

print factors
