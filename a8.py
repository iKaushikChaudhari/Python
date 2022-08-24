def slen(str1):
    l=0
    for ch in str1:
        l=l+1
        return l
def scat(str1,str2):
    str3=str1+str2
    return str3
def srev(str1):
    str2=""
    for ch in str1:
        str2=ch+str2
    return str2
def chk_pal(str1):
    str2=srev(str1)
    if str1==str2:
        print(" is palindrome")
    else:
        print(" is not palindrome")
    return str1
print('''*******MENU*******
1. String lenght
2. String compare
3. String concadination
4. String reverse
5. String plaindrome
6. String case change''')
choice=int(input("Enter your choice from menu ="))
if (choice==1):
    str1=input("Enter the string=")
    l=slen(str1)
    print("lenght of string is",l)
if (choice==2):
    str1=input("Enter the string=")
    str2=input("Enter the string=")
if str1==str2:
    print("strings are equal")
else:
    print("strings are not equal")
if (choice==3):
    str1=input("Enter the string=")
    str2=input("Enter the string=")
    print(scat(str1,str2))
if (choice==4):
    str1=input("Enter the string=")
    print(srev(str1))
if (choice==5):
    str1=input("Enter the string=")
    print(chk_pal(str1))
if (choice==6):
    str1=input("Enter the string=")
    print("lower case=",str1.lower())
    print("upper case=",str1.upper())