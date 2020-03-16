s=''
for i in range(1,int(input())+1):
    print(int(s+str(i)+s[::-1]))
    s=s+str(i)
