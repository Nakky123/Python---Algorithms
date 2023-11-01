n = int(input())
count = 0

for a in range(1, n):
    for b in range(a, n):
        c = n - a - b
        if c < b:
            break
        if a + b > c:
            count += 1

print(f"Number of triangles that can be created: {count}")
