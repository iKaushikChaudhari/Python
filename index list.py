list1=[11,22,44,12,45,56,84,65,32,21,23,24,55]
print (list1)
num=int(input("Enter Number: "))
if num in list1:
    print(num," Number Exit in list")
    index = list1.index(num)
    print("The Position Of Number Is ",index)
else:
    print(num," The Number Does Not Exist In List")
