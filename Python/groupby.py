from itertools import groupby
for i ,j in groupby(input()):
    s=(len(list(j)),int(i))
    print(s,end=' ')
