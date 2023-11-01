def finding(n):
    total = 0
    for i in range(1,n+1):
        if n % i == 0 :
            total += 1
    return total
n = int(input())
import time
start = time.time()
print(finding(n))
end = time.time()
print(f"solve() elapsed time : {end - start}")