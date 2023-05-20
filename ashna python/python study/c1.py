class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def peri(self):
        return(2*(self.length+self.breadth))
a=int(input("enter length of rectangle1:"))
b=int(input("enter breadth of rectangle1:"))
c=int(input("enter length of rectangle2:"))
d=int(input("enter breadth of rectangle2:"))
rectangle1= Rectangle(a,b)
rectangle2= Rectangle(c,d)
area1= Rectangle.area(rectangle1)
area2= Rectangle.area(rectangle2)
peri1= Rectangle.peri(rectangle1)
peri2= Rectangle.peri(rectangle2)
print("area of r1:",area1)
print("area of r2:",area2)
print("peri ofr1:",peri1)
print("peri of r2:",peri2)
if(area1>area2):
    print("r1 is greater")
elif(area1<area2):
    print("r2 is greater")
else:
    print("both are equal")
    
