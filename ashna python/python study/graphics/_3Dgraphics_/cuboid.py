l=int(input("enter the length of the cuboid:"))
b=int(input("enter the breadh of the cuboid:"))
h=int(input("enter the hieght of the cuboid:"))

def area(l,b,h):
    return(2*((l*b)+(b*h)+(l*h)))
print("area:",area(l,b,h))

def peri(l,b,h):
    return(4*(l+b+h))
print("perimeter:",peri(l,b,h))
