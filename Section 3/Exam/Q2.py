import random
def median(S):
    return S[(len(S)-1)//2]

def generate(SEED, MIN, MAX, N):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N)

SEED, MIN, MAX, N, K = 2022, 10, 100, 10, 5
S = generate(SEED, MIN, MAX, N)
S.sort()

for i in range(K-1):
    S.remove(median(S))

print(median(S))