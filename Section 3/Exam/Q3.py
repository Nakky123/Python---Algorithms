import random
def generate(SEED, MIN, MAX, N):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N)

def median(s) :
    s.sort()
    lst = []
    while len(s) > 0 :
        mid = (len(s) -1)//2
        lst.append(s[mid])
        s.remove(s[mid])
    return lst

SEED, MIN, MAX, N, K = map(int,input().split())
S = generate(SEED, MIN, MAX, N)
deleted_median = median(S)
print(deleted_median[K - 1])