n=int(input())
s=ord('a')
width=4*(n-1)+1
l=[]
count=s+n-1
st=chr(count)
print(st.center(width,'-'))
for i in range(1,n):
    rev=st[::-1]
    a=len(st)//2
    st=st[:a+1]+"-"+chr(count-i)+"-"+rev[:a+1]
    print(st.center(width,'-'))

