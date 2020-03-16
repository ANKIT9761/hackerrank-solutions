n=int(input())
for i in range(n):
    a,c=int(input()),set(map(int,input().split()))
    b,d=int(input()),set(map(int,input().split()))
    if(c.issubset(d)):
        print("True")
    else:
        print("False")
    
