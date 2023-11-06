def is_hex_palindrome(n):
    hex_value = hex(n)[2:]
    return hex_value == hex_value[::-1] 
N = int(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if is_hex_palindrome(num):
        count += 1
print(count)
