def solve(s):
    for i in range(len(s) - 1):
        minv, minj= s[i], i
        for j in range(i +1, len(s)):
            if s[j] > minv:
                minv, minj = s[j], j
        if i != minj:
            s[i], s[minj] = s[minj], s[i]
    return s
    

s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])

print(solve(s))