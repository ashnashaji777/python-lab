import csv
f=open("file.csv","r")
csvfile=csv.reader(f)
for i in csvfile:
    print(i)
f.close()    
