n1=int(input('Enter first number'))
n2=int(input('Enter second number'))
for i in range(n1,n2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)