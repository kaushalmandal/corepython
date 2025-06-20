n=int(input('Enter any number from user'))
rem=0
result=0
while n>0:
    rem=n%10
    result=result*10+rem
    n=n//10
print(result)