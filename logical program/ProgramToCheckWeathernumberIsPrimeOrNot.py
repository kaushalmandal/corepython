n=int(input('Enter any number'))
i=1
count=0
while i<=n:
    if n%i==0:
        count=count+1
        i=i+1
if count==2:
    print('prime no',n)
else:
    print('not prime',n)