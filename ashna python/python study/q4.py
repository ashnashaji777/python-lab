import csv
f=open("file.csv","r")
csvfile=csv.DictReader(f)
a=input("enter the colomn name(name,age,bg):")
for i in csvfile:
    print(i[a])
f.close()    
