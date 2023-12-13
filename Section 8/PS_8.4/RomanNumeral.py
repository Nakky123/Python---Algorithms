def solve(roman) : 
    T = {"I" : 1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M" : 1000}
    s = 0

    for i in range(0,len(roman) - 1) :
        # print(roman[i] ,":", T[roman[i]],roman[i+1],":",T[roman[i+1]])
        if T[roman[i]] < T[roman[i + 1]] :
            s -= T[roman[i]]
            # print("s - :",s)
        else :
            s += T[roman[i]]
            # print("s + :",s)
        # print("s :",s)
    s += T[roman[i + 1]]
    # print(T[roman[i+1]],s)
    # print(T[roman[-1]])
    return s 

N = input()
print(solve(N))