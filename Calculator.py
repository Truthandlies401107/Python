a = input("Enter the first number: ")
b = input("Enter the second number: ")
print("Following are some choice: ")
print("1.Addition.")
print("2.Subraction.")
print("3.Multiplication.")
print("4.Division.")
ch = int(input("Enter your choice: "))

if ch == 1:
    sum = int(a)+int(b)
    print("The sum of two number is: ", sum)

if ch == 2:
    sum = int(a)-int(b)
    print("After subracting two numbers we get: ",sum)

if ch == 3:
    product= int(a)*int(b)
    print("The product of two number: ", product)

if ch == 4:
    product = int(a) / int(b)
    print("The division product is: ", product)

