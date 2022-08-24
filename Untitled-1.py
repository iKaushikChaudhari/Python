num = int(input('Enter the number : '))
if num>0 and num <10 : 
	print(num," is one digit number")
	print("The square of ",num,"is : ",num**2)

elif num>9 and num<100 :
	print(num," is a two digit number")
	print("Square root of ",num, "is : ",round(num**0.5))
	
elif num>99 and num<1000 : 
	print(num," is a three digit number")
	print("Cube root of ",num,"is : ",round(num**(1/3)))

else :
	print("Enter Correct Number")
