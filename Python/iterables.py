from itertools import combinations
N=int(input())
L=input().split()
K=int(input())
C=list(combinations(L,K))
F=list(filter(lambda c:'a' in c,C))
print(len(F)/len(C))
