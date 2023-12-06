fn = 0
sn = 1
n = int(input("Enter no. of terms: "))
print("The fibonnanci series: ")
for i in range(1, n):
    nn = int(fn) + int(sn)
    print(" ",nn)
    fn = sn
    sn = nn

