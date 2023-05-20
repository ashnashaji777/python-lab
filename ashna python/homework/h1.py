class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def peri(self):
        return(2*(self.length+self.breadth))
l1=int(input("enter the length of rectangle one:"))
b1=int(input("enter the breadth of rectangle one:"))
l2=int(input("enter the length of rectangle two:"))
b2=int(input("enter the breadth of rectangle two:"))
rectangle1= Rectangle(l1,b1)
rectangle2= Rectangle(l2,b2)
area1= Rectangle.area(rectangle1)
area2= Rectangle.area(rectangle2)
print("area of rectangle one:",area1)
print("arae of rectangle two:",area2)
if(area1>area2):
    print('rectangle one is bigger')
else:
    print('rectangle two is bigger')
peri1= Rectangle.peri(rectangle1)
peri2= Rectangle.peri(rectangle2)
print("perimeter of rec1:",peri1)
print("perimeter of rec2:",peri2)
    
