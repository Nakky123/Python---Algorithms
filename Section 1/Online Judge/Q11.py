def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input(""))

if is_prime(n):
    print("The number is prime.")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
