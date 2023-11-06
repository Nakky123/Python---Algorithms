def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            if prime(i):
                factors.append(i)
                n //= i
        i += 1
    return factors

number = int(input())
factors = prime_factors(number)
print(*factors)
