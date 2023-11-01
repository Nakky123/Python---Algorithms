def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def longest_collatz_sequence(N, M):
    max_length = 0
    max_number = 0
    for i in range(N, M + 1):
        current_length = collatz_length(i)
        if current_length > max_length:
            max_length = current_length
            max_number = i
        elif current_length == max_length:
            max_number = max(max_number, i)

    return max_number, max_length


N, M = map(int, input().split())

result, length = longest_collatz_sequence(N, M)
print(result)
print(length)
