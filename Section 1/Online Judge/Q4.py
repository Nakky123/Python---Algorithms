def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
N, M = map(int, input().split())
count = 5
largest_primes = []
for num in range(M, N - 1, -1):
    if is_prime(num):
        largest_primes.append(num)
        if len(largest_primes) == count:
            break
for prime in largest_primes:
    print(prime , end=" ")
    
