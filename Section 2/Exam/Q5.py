def ackermann(n, m, counts):
    if n == 0:
        counts += 1
        return m + 1, counts
    elif n > 0 and m == 0:
        counts += 1
        return ackermann(n - 1, 1, counts)
    else:
        counts += 1
        temp, counts = ackermann(n, m - 1, counts)
        return ackermann(n - 1, temp, counts)

n, m = map(int, input().split())

result, counts = ackermann(n, m, 0)
print(result)
print(counts)
