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

# Read input
N, M = map(int, input().split())

# Count the numbers that satisfy the conditions
count = 0
for i in range(M // 2):
    if all(prime(factor) for factor in prime_factors(i)):
        count += 1

# Print the count
print(count )
