#Enter some sentence from user kaushal kumar mandal
# lahsuak ramuk ladnam

s=input('Enter some sentence from user')
l=s.split()
l1=[]
# i=0
# while i<len(l):
#     l1.append(l[i][::-1])
#     i=i+1
# output=' '.join(l1)
# print(output)


for x in range(len(l)):
    l1.append(l[x][::-1])
output=' '.join(l1)
print(output)