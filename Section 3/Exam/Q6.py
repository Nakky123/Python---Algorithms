def insertionsort(n,s):
    cnt = 0
    for i in range(1, n):
        
        j, val = i -1, s[i]
        cnt +=1
        if cnt == k :
                return s[j + 1],s[i]
        while j >= 0 and s[j] > val:
            s[j+1] = s[j]
            j -= 1
            cnt += 1
            if cnt == k :
                return s[j + 1],s[i]
        s[j + 1] = val

n , k = map(int,input().split())
s = list(map(int, input().split()))
result = insertionsort(n,s)
print(*result)