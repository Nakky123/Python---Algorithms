import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n, m = map(int, input().split())

count_x = 0
count_y = 0

for i in range(1,int(m ** 0.5) + 1):
    if is_prime(i):
        if i**2 < m:
            count_x+= (int(math.log(m ,i)) - 1)
for i in range(1,int(n ** 0.5) + 1):
    if is_prime(i):
        if i**2 < n:
            count_y+= (int(math.log(n ,i)) - 1)

print(count_x - count_y)