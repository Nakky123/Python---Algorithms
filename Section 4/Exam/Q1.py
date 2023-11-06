import random

SEED, MIN, MAX, N = 2022, 10, 30, 10

random.seed(SEED)

S = random.sample(range(MIN, MAX), N)

X = random.sample(range(MIN, MAX), N)

output = []
for element in X:
    try:
        index = S.index(element)
        output.append(str(index))
    except ValueError:
        output.append("-1")

print(" ".join(output))
