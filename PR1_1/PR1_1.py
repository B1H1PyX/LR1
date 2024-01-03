a = int(input("Insert a: "))
b = int(input("Insert b: "))
x = 0
if a > 0:
    if b > 0:
        if a > b:
            x = a * b - 1
        elif a == b:
            x = 255
        else:
            x = (a - 5) / b
        print("X =", x)
    else: 
        print("Insert b > 0")
else:
    print("Insert a > 0")