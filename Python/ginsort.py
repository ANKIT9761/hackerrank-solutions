a=input()
u=[]
l=[]
d=[]
for i in a:
    if(i.isupper()):
        u.append(i)
    elif(i.islower()):
        l.append(i)
    elif(i.isdigit()):
        d.append(i)
u.sort()
l.sort()
d.sort(key=lambda x:(int(x)%2==0))
print("".join(l)+"".join(u)+"".join(d))
