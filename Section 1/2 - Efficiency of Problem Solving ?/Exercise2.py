def adding(a):
    total = 0 
    for i in range(a+1):
        total += i  
    return total
a = int(input("Enter an integer: "))
c = adding(a)
print(c)
