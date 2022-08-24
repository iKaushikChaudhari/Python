class circle:
    def area(self,radius):
        self.radius=radius
        a=3.14*self.radius*self.radius
        print("Area Of Circle :",a)
class square:
    def area(self,side):
        self.side=side
        a=self.side*self.side
        print("Area Of Square :",a)
class rectangle:
    def area(self,len, breath):
        self.len=len
        self.breath=breath
        a=self.breath*self.breath
        print("Area Of Rectangle :",a)

c=circle()

choice=0
while(choice!=5):
    choice=int(input("***Enter Your Choice*** \n 1 create Account\n 2 chek\n 3 dep \n 4 with\n 5 exit "))
    if(choice==1):
        cn=input("Enter Name :")
        ca=input("Enter Address :")
        an=eval(input("Enter Account Number :"))
        cb=eval(input("Enter Initial Balance :"))
        ob.acc_create(cn,ca,an,cb)
    if(choice==2):
        ob.chkbal()
    if(choice==3):
        v=eval(input("Enter Deposit Amount :"))
        ob.deposit(v)
    if(choice==4):
        amt=eval(input("Enter Withdraw Amount :"))
        ob.withdraw(amt)
        ob.upbal()
 