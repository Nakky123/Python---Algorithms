def sorting_char(s):
    upper_char = []
    lower_char = []
    for char in s:
        if char.isupper():
            upper_char.append(char)
        elif char .islower():
            lower_char.append(char)
    upper_char.sort()
    lower_char.sort(reverse=True)
    print("".join(upper_char) + "  " + "".join(lower_char))
S = input()
sorting_char(S)