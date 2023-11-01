def sum1(n , m):
    s = 0
    for i in range(n , m + 1):
        s += i
    return s

print(sum1(1,5))