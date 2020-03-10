m,s1=int(input()),set(input().split())
n,s2=int(input()),set(input().split())
s1.symmetric_difference_update(s2)

l=list(map(int,s1))
l.sort()

for i in l:
    print(i)
