s=input('Enter main string')
sub=input('Enter substring')
i=s.find(sub)
if i==-1:
    print('Not Found')
while i!= -1:
    print(sub,'present at',i)
    i=s.find(sub,i+len(sub),len(s))

