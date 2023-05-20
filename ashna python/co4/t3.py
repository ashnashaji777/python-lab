class rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area(self):
        self.__area=self.__length*self.__width
        print("area is:",self.__area)
    def __lt__(self,other):
        if self.__area<other.__area:
            return True
        else:
            return False
l1=int(input("enter the length of rectangle1:"))
b1=int(input("enter the width of rectangle 1:"))
l2=int(input("enter the length of rectangle 2:"))
b2=int(input("enter the width of rectangle 2:"))
o1=rectangle(l1,b1)
o2=rectangle(l2,b2)
o1.area()
o2.area()
if o1<o2:
    print("rectangle two is large")
elif o1>o2:
    print("rectangle 1 is large ")
else:
    print("both are equal")














