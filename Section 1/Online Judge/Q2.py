import random
import time
def generate_random_list(SEED, MIN, MAX, N):
    random.seed(SEED)
    randomz = random.sample(range(MIN, MAX), N)
    return randomz
start = time.time()
SEED, MIN, MAX, N = map(int, input().split())
random_list = generate_random_list(SEED, MIN, MAX, N)
print(min(random_list) , random_list.index(min(random_list)))
end = time.time()
print(end - start)
