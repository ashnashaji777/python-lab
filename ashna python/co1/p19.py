list=[11,52,47,6,35,78,94,25,9,96]
print(list)
for i in list:
    if(i%2==0):
        list.remove(i)
print("list after removing even number:")
print(list)
