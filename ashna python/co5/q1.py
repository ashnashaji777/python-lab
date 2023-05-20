f=open("file1.txt","r")
list=[]
for i in f:
    list.append(i)
f.close()
print(list)
    
