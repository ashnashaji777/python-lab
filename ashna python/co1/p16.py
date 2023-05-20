a={"jan":31,"feb":28,"march":31,"april":30,"june":30}
l=list(a.items())
l.sort()
print("ascending order is\n",l)
l=list(a.items())
l.sort(reverse=True)
print("descending order is\n",l)
dict=dict(l)
print("dictionary",dict)
