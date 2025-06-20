s=input('Enter some string from user')
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in s1:
    output=output+x
for x in s2:
    output=output+x
print(output,end=' ')