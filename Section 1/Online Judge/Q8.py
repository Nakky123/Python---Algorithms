def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_twin_primes(n):
    twin_primes = []
    for i in range(3, n + 1):
        if is_prime(i) and is_prime(i - 2):
            twin_primes.append((i - 2, i))
    return twin_primes

n = int(input())
twin_prime_pairs = find_twin_primes(n)

for pair in twin_prime_pairs:
    print(pair[0], pair[1])

print(len(twin_prime_pairs))