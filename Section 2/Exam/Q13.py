def sumz(a):
    total = 0
    for i in range(1,a+1):
        total += i
    return total
n = int(input())
print(sumz(n))