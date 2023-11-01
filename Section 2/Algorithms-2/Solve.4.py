def hanoi(n , src , via , dst):
    if n ==1 :
        print(f"{src} -> {dst}")
    else :
        hanoi(n-1, src, dst, via)
        hanoi(1 , src, via, dst)
        hanoi(n-1, via, src, dst)
        
n = int(input())
print((2 ** n) - 1)
hanoi(n , "A", "B", "C")

