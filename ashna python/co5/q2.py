f1=open("file2.txt","r")
f2=open("file3.txt","w")
count=1
for i in f1:
    if count % 2!=0:
        f2.write(i)
    count=count+1
f1.close()
f2.close()

f2=open("file3.txt","r")
for i in f2:
    print(i)
f2.close()    
