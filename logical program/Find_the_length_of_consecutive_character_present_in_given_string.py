s=input('Enter some string from user')
l=list(s)
count=1
max_count=1
res=[]
for x in range(len(l)-1):
    if l[x]==l[x+1]:
        count=count+1
        if count>max_count:
            max_count=count
    else:
        res.append((l[x],count))
        count=1
res.append((l[len(l)-1],count))
d=dict(res)
max_value=0
char=None
for k,v in d.items():
    if v>max_value:
        max_value=v
        char=k

print(f"max consecutive char is {char} and his count is {max_value}")