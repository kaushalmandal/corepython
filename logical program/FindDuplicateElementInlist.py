l=eval(input('Enter the list from user'))
l1=[]
for x in l:
    if l.count(x)>1:
        if x not in l1:
            l1.append(x)
print(l1)