
LIMIT = 4000000

list = []
x = 1
y = 2
fib = 0

list.append(y)

while fib < LIMIT:
    print "fib = {0} x = {1} y = {2}".format(fib, x, y)
    fib = x + y
    x = y
    y = fib

    if (fib < LIMIT) and (fib % 2 == 0):
        list.append(fib)
        print list

sum = sum(list)

print sum
