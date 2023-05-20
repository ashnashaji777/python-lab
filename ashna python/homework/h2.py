class rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        self.__area=self.__length*self.__breadth
        print("area:",self.__area)
    def __it__(self,other):
        if self.__area<other.__area:
            return True
        else:
            return False
        
l1=int(input("enter the length of rectangle1:"))
b1=(input("enter the breadth of rectangle1:"))
l2=int(input("enter the length of rectangle2:"))
b2=int(input("enter the breadth of rectangle2:"))
o1= rectangle(l1,b1)
o2= rectangle(l2,b2)
o1.area()
o2.area()
if o1<o2:
    print("rectangle2 is bigger")
else:
    print("rectangle2 is bigger")

    
