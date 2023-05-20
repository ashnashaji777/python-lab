import csv
fields = ['username','age','course']
users=[{"username":"ashna","age":"21","course":"mca"},
       {"username":"ameena","age":"21","course":"ttc"},
        {"username":"achu","age":"23","course":"Btech"}]
a=open("file.csv","w")
csvfile = csv.DictWriter(a,fieldnames=fields)
csvfile.writeheader()
csvfile.writerows(users)
a.close()
a=open("file.csv","r")
csvv=csv.DictReader(a)
for i in csvv:
    print(i)
a.close()     
 
