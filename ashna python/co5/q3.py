import csv
f=open("file.csv","r")
csvfile = csv.DictReader(f)
a=input("enter colomn name(name,dob,age):")
for i in csvfile:
    print(i[a])
a.close()

