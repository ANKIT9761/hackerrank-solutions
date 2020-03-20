from itertools import product
from time import time

a,n=list(map(int,input().split()))
a=[list(map(int,input().split()))[1:] for i in range(a)]
results=map(lambda x:sum(i*i for i in x)%n,product(*a))
print(max(results))



