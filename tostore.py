import os
print("Hello World")

def multiplicationTable(n):
    os.system("cls")
    print("\n")
    print("-----------------Multiplication Table for",n,"-----------")
    print()
    for i in range(1,10+1):
        print(f"\t\t{n} X {i} = {i*n}")

    print()

num = int(input("Enter number : "))

multiplicationTable(num)