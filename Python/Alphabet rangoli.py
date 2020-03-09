def print_rangoli(n):
    s=ord('a')
    width=4*(n-1)+1
    count=s+n-1
    l=[]
    st=chr(count)
    l.append(st.center(width,'-'))
    for i in range(1,n):
        a=len(st)//2
        st=st[:a+1]+"-"+chr(count-i)+"-"+st[:a+1][::-1]
        l.append(st.center(width,'-'))
    for i in l[::-1][1:len(l)]:
        l.append(i)
    for i in l:
        print(i)





        


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
