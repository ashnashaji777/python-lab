list=[]
num=int(input("enter the number of elements in the list:"))
print("enter the",num,"elements")
for i in range(num):
    n=int(input())
    list.append(n)
sum=0
for i in list:
        sum=sum+i
print("the sum of",num,"'elements in the list is",sum)
