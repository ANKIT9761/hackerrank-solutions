a=set(map(int,input().split()))
n=int(input())
c=0
for i in range(n):
    b=set(map(int,input().split()))
    if(len(a)==len(b)):
        print("False")
    elif(a.issuperset(b)):
        c=c+1
if(c==n):
    print("True")
else:
    print("False")
