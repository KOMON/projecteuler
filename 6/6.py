
num = 0
num2 = 0
for x in range(1,101):
    num += x**2
    num2 += x

num2 *= num2

print num2 - num


