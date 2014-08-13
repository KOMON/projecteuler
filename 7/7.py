
SAMPLE = 10001

primes = []

primes.append(2)
primes.append(3)

counter = 5

while len(primes) < SAMPLE:
    if counter % 2 != 0 and counter % 3 != 0:
        temp = 5
        while temp**2 <= counter:
            if counter % temp == 0:
                break;
            temp += 2
        if temp**2 > counter:
            primes.append(counter)
    counter += 2

print max(primes)
