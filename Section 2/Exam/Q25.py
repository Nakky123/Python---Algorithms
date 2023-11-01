def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)
def find_solution(A, B, C):
    gcd, x, y = extended_gcd(A, B)
    if C % gcd != 0:
        return "No solution exists."
    else:
        x0 = x * (C // gcd)
        y0 = y * (C // gcd)
        return x0, y0
A, B, C = map(int, input().split())
solution = find_solution(A, B, C)
print(f"{solution[0]} {solution[1]}")
