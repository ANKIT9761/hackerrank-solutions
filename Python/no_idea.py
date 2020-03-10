hap=0
n,m=input().split()
array=input().split()
set_a=set(input().split())
set_b=set(input().split())
for i in range(len(array)):
    if(array[i] in set_a):
        hap=hap+1
    elif(array[i] in set_b):
        hap=hap-1
    else:
        continue
print(hap)
