list1 = [10,11,12,14,15,18,19,22,25,30,36,45,55]
print(list1)
num=int(input("Enter Number: "))
hight= len(list1)
low=0
mid = (hight+low)//2
if num == list1[mid]:
    print("num is in mid")
elif num > list1[mid]:
    low = mid +1
    if num == list1[low]:
        print("hello")
    
elif num < list1[mid]:
    high = mid-1
    if num == list1[high]:
        print("bye")