# Enter the sentence from user kaushal kumar mandal
# ladnam ramuk lahsuak

s=input('Enter the sentence from user')
l=s.split()
i=len(s)-1
output=''
while i>=0:
    output=output+s[i]
    i=i-1
result=''.join(output)
print(result)