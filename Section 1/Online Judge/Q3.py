def findDivisor(a):
    total = 0
    sqrtz = int(a ** 0.5)
    for i in range(1, sqrtz + 1):
        if a % i == 0:
            total += i
            total += a // i
    return total
num = int(input())
print(findDivisor(num))


