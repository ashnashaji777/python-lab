l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))

def area(l,b):
    return(l*b)
print("area of rectangle:",area(l,b))

def peri(l,b):
    return(2*(l+b))
print("perimetr of rectangle:",peri(l,b))
