from collections import defaultdict

def print_anagrams(N, words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word))].append(word)

    result = []
    for anagram_list in sorted(anagrams.values()):
        result.append(f"{anagram_list[0]} {len(anagram_list)}")
    print('  '.join(result))

N, *words = input().split()
print_anagrams(int(N), words)
