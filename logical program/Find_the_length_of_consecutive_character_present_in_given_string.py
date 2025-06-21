s=input('Enter some string from user')
l=list(s)
count=1
res=[]
for x in range(len(l)-1):
    if l[x]==l[x+1]:
        count=count+1
    else:
        res.append((l[x],count))
        count=1
res.append((l[len(l)-1],count))
print(res)