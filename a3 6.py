n=int(input("Enter number of rows for ABCD pattern :"))
for i in range (1,n+1):
    v=65
    for j in range (1,i+1):
        print(chr(v),end=" ")
        v += 1
    print()