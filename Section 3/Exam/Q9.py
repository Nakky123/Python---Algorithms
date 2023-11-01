n = int(input())
data = list(map(int, input().split()))
data_sorted = sorted(data)
for num in data:
    print(num, end=' ')
print()
for num in data_sorted:
    print(num, end=' ')
