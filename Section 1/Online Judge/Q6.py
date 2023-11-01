def findDivisor(a):
    total = 0
    sqrtz = int(a ** 0.5) + 1
    for i in range(1, sqrtz):
        if a % i == 0:
            total += i
            if i != a // i:
              total += a // i
    return total
num = 20
print("Sum of divisors:", findDivisor(num))