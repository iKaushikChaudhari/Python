numl=int(input("Enter First Number")) 
num2=int(input("Enter Second Number")) 
print("First Number Is.",numl) 
print("Second Number Is.",num2) 
if(numl>num2):
    print("Square Of Smaller Number:",num2**2) 
    print("Cube Of Greater Number:",numl**3) 
elif(num2>numl):
    print("Square Of Smaller Number:",numl**2)
    print("Cube Of Greater Number:",num2**3) 
else:
    print("Both Numbers Are Equal")
    print("Square Of Number:",numl**2)
    print("Square Root Of Number:",numl**0.5)
    print("Cube Root Of Number:",numl**(1/3)) 