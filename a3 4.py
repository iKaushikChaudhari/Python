count=1
row=int(input("Enter Number Of Row :"))
column=int(input("Enter Number Of Column :"))
for i in range (0,row):
    for j in range (0,column):
        print (count ,end=" ")
        count = count+1
    print()