def solve(n):
    anagrams = set([])
    total = []
    for _ in range(n):
        word1 = input()
        word2 = "".join(sorted(word1))
        if word2 not in anagrams:
            total.append(word1)
            anagrams.add(word2) 
    print(*total)
N = int(input())
solve(N)