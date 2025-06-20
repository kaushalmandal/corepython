s=input('Enter some string from user')
d={}
for x in s:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,'------',v)