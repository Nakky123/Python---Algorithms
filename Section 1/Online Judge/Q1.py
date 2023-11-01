def sum_num(n ,m):
    sum_of_numbers = ((m - n + 1) * (n + m)) // 2
    return sum_of_numbers
n , m = map(int , input().split())
print(sum_num(n,m))