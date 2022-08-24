class bank:
    def __init__(self):
        self.cn=" "
        self.ca=" "
        self.an=0
        self.cb=0
    def acc_create(self,cn,ca,an,cb):
        self.cn=cn 
        self.ca=ca
        self.an=an
        self.cb=cb
    def chkbal(self):
        print("Customer Name : ", self.cn)
        print("Customer Address : ",self.ca)
        print("Customer Account Name : ",self.an)
        print("Customer Bank Balance : ",self.cb)
    def upbal(self):
        print("Customer Updated Balance ",self.cb)
class cust(bank):
    def withdraw (self,amt):
        self.cb=self.cb-amt
    def deposit (self,amt):
        self.cb=self.cb+amt

ob=cust()
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
 