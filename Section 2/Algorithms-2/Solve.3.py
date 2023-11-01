def zz(N):
    total = [N]  
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
print(*result_list)
print(len(result_list))
