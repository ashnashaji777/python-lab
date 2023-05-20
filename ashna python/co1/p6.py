l1=[1,2,5,4,6,7]
l2=[3,5,8,9,2,1]
if(len(l1)==len(l2)):
    print("same length")
else:
    print("different length")
if(sum(l1))==sum(l2):
    print("same sum")   
else:
    print("different sum")
    print("common",set(l1).intersection(set(l2)))    
