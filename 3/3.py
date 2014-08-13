import math

SAMPLE = 600851475143
LIMIT = math.sqrt(SAMPLE)
factors = []

d = 2

while d <= LIMIT:
    if SAMPLE % d == 0:
        factors.append(d)
        SAMPLE /= d
    d += 1

print factors
print max(factors)


