def zz(N):
    total = []  
    while N != 1:
        if N % 2 == 0:
            N //= 2
            total.append(N)
        else:
            N = 3 * N + 1
            total.append(N)
    return total

n = int(input())
result_list = zz(n)
count = 0
for i in result_list:
    if i % 2 == 0:
        count += 1
print(result_list)
print(count)
