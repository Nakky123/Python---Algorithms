import random

def generate(SEED, MIN, MAX, N):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N)

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes

def count_elements_with_prime_factors(S):
    max_element = max(S)
    primes = sieve_of_eratosthenes(max_element)
    count = 0
    for num in S:
        prime_factor_count = 0
        for prime in primes:
            if prime > num:
                break
            if num % prime == 0:
                prime_factor_count += 1
        if prime_factor_count > 0 and all(prime % i != 0 for i in range(2, prime)):
            count += 1
    return count

SEED, MIN, MAX, N = 2022, 10, 100, 15
S = generate(SEED, MIN, MAX, N)
output = count_elements_with_prime_factors(S)
print(output - 1)
