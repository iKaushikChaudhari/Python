matrix1=[]
matirx2=[]

row=int(input("\n Enter Row"))
col=int(input("\nEnter Colume"))
choice=0
while(choice!=3):
    print("1 addition \n2 multi")
    choice=int(input("choice:"))
    if choice==1:
        print("Enter elements of Matirx 1 ")
        for i in range(row):
            r=[]
            for j in range(col):
                element1=int(input())
                r.append(element1)
            matrix1.append(r)
        
        print("Enter elements of Matirx 2 ")
        for i in range(row):
            r=[]
            for j in range(col):
                element2=int(input())
                r.append(element2)
            matirx2.append(r)

        # print first matrix 
        print("\n Matrix1:")
        for i in range (row):
            for j in range (col):
                print(matrix1[i][j],end=" ")
            print()
        
        # print second matrix
        print("\n Matrix2:")
        for i in range (row):
            for j in range (col):
                print(matirx2[i][j],end=" ")
            print()
        
        print("\n The Addition Of Two Matrices: ")
        for i in range(row):
            for j in range (col):
                print(matrix1[i][j] + matirx2[i][j],end=" ")
            print()
    
    elif choice==2:
        print("Enter elements of Matirx 1 ")
        for i in range(row):
            r=[]
            for j in range(col):
                element1=int(input())
                r.append(element1)
            matrix1.append(r)
        
        print("Enter elements of Matirx 2 ")
        for i in range(row):
            r=[]
            for j in range(col):
                element2=int(input())
                r.append(element2)
            matirx2.append(r)

        # print first matrix 
        print("\n Matrix1:")
        for i in range (row):
            for j in range (col):
                print(matrix1[i][j],end=" ")
            print()
        
        # print second matrix
        print("\n Matrix2:")
        for i in range (row):
            for j in range (col):
                print(matirx2[i][j],end=" ")
            print()
        
        print("\n The Multiplication Of Two Matrices: ")
        for i in range(row):
            for j in range (col):
                print(matrix1[i][j] * matirx2[i][j],end=" ")
            print()
