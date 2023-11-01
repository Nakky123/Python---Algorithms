def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def mersenne_primes(N):
    mersenne_primes_list = []
    p = 2
    while True:
        mersenne_number = 2**p - 1
        if mersenne_number > N:
            break
        if is_prime(mersenne_number):
            mersenne_primes_list.append(mersenne_number)
        p += 1
    return mersenne_primes_list

N = int(input(""))
mersenne_primes_list = mersenne_primes(N)
for mersenne_prime in mersenne_primes_list:
    print(mersenne_prime)
