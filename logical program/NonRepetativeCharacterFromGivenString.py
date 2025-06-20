s=input('Enter some string from user')
l1=[]
for x in s:
    if s.count(x)<=1:
        l1.append(x)
output=''.join(l1)
print(output)

