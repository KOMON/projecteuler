
palindromes = []

def isPalindrome(n):
    x = str(n)
    y = x[::-1]
    if (x == y):
        return True
    else:
        return False


for n in range(100,999):
    for m in range(100,999):
        x = n*m
        if isPalindrome(x):
            palindromes.append(x)

print max(palindromes)
