class circle :
    def area(self,radius):
        self.radius=radius
        a=3.14*self.radius**2
        print("Area OF Circle : ",a)
class square :
    def area(self,side):
        self.side=side
        a=side**2
        print("Area Of Square : ",a)
class rectangle :
    def area(self,lenght,breath):
        self.lenght=lenght
        self.breath=breath
        a=self.lenght*self.breath
        print("Area OF Rectangle : ",a)
c=circle()
s=square()
r=rectangle()
ch=0
while ch != 4:
    ch=int(input('''\n***Enter Your Choice***
    1. To Find Area OF Circle
    2. To Find Area Of Square
    3. To Find Area Of Rectangle
    4. Exit \n'''))
    if ch==1:
        radius = int(input("Enter Radius: "))
        c.area(radius)
    elif ch==2:
        side=int(input("Enter Side: "))
        s.area(side)
    elif ch==3:
        lenght=int(input("Enter Lenght: "))
        breath=int(input("Enter Breath: "))
        r.area(lenght,breath)
