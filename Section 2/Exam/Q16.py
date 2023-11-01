def num(n):
    total = []
    for i in range(n, 0, -1):
        total.append(i)
    return total

n = int(input())
print(*num(n))
