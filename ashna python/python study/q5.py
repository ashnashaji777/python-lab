import csv
fields=['name','age','bg']
users=[{"name":"tanku","age":5,"bg":"O"},{"name":"loozy","age":3,"bg":"A"},{"name":"chakkara","age":2,"bg":"B"}]
f=open("file.csv","w")
csvfile=csv.DictWriter(f,fieldnames=fields)
csvfile.writeheader()
csvfile.writerows(users)
f.close()
f=open("file.csv","r")
csvv=csv.DictReader(f)
for i in csvv:
    print(i)
f.close()    

