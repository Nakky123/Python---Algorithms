def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

A, B, K = map(int, input().split())
count = 0
kth_prime = None
for num in range(max(2, A), B + 1):
    if is_prime(num):
        count += 1
        if count == K:
            kth_prime = num
            break
prime_sum = sum(filter(is_prime, range(A, B + 1)))
if kth_prime is not None:
    print(prime_sum)
    print(kth_prime)
else:
    print(prime_sum)
    print(-1)
