s={x for x in[1,4,6,-5,8,5,-7,9] if x>0}
print(s)
y={x for x in[1,5,8,-7,9,-3,6,-1] if x<0}
print(y)
s=[x**2 for x in range(10)]
print(s)
a=[x**3 for x in range(6)]
print(a)
q={x for x in "asaghdhsfyewmsckllsufpoqikcmbsyvhu" if x not in 'aeiou'}
print(q)
r={ x for x in "wshfueyuyggf" if  x not in 'abcde'}
print(r)
d=[ord(x) for x in 'dog']
print(d)