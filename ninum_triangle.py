
print("Following are some choices: ")
print("1. Normal Triangle.")
print("2. Inverted Triangle.")
ch = int(input("Enter your choice: "))
n = int(input("Enter the no. of rows: "))
if ch == 1:
    for i in range(0,n):
        for j in range(0,(i+1)):
            print("1 ", end="")
        print("\r")
if ch == 2:
     for i in range(n,0,-1):
        for j in range(0,i):
            print("1 ", end="")
        print("\r")
