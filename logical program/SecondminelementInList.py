l=eval(input('Enter list from user'))
min=l[0]
for x in l:
    if x<min:
        min=x
print('minimum element in list is :',min)
l.remove(min)
secmin=l[0]
for x in l:
    if x<secmin:
        secmin=x
print('secmin element in list is :',secmin)