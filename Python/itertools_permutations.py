from itertools import permutations
a,b=list(input().split())
for _ in sorted(list(permutations(a,int(b)))):
    print("".join(_))
