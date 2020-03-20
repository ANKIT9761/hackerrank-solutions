from itertools import combinations
a,b=list(input().split())
a=[_ for _ in a]
a.sort()
for i in range(1,int(b)+1):
    c=list(map(lambda x:"".join(x),combinations(a,i)))
    for _ in c:
        print(_)
