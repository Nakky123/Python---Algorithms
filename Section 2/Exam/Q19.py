import string

alphabet = string.ascii_uppercase

for i in range(len(alphabet), 0, -1):
    print(' '.join(alphabet[:i]))

