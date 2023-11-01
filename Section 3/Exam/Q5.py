def bubblesort(n,s,k):
    cnt = 0
    for i in range(n -1):
        for j in range(n -1 -i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j] 
                cnt +=1
                if cnt == k :
                    return s[j],s[j+1]

n , k = map(int,input().split())
s = list(map(int, input().split()))
result = bubblesort(n,s,k)
print(*result)