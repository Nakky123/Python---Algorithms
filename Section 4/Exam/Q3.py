import time
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def solve(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_palindromes(start, end):
    count = 0
    for i in range(start, end+1):
        if is_palindrome(i) and solve(i):
            count += 1
    return count

start, end = map(int, input().split())
print(count_palindromes(start, end))

