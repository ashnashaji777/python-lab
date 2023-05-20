l=[]
n=6
print("enter the numbers")
for i in range(n):
    num=int(input("number:"))
    l.append(num)
print(l)
for i in range(len(l)):
     if(l[i]>500):
      l[i]="over"
print(l)    
