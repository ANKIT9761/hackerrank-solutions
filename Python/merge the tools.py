def dup(a):
    t=[]
    for i in a:
        if(i not in t):
            t.append(i)
    return "".join(t)

def merge_the_tools(string, k):
    l1=int(len(string)/k)
    l=[]
    for i in range(0,l1):
        a=string[k*i:k*i+k]
        b=dup(a)
        print(b)
