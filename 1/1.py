
list = []

for x in range(1, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
        list.append(x)

sum = sum(list)


print sum
