def minion_game(string):
    vow='AEIOUaeiou'
    stuart=[]
    kevin=[]
    for i in range(len(string)):
        e=''
        if (string[i] in vow):
            for j in range(i,len(string)):
                e+=string[i]
                kevin+=[e]
        else:
            for j in range(i,len(string)):
                e+=string[i]
                stuart+=[e]

    if(len(kevin)>len(stuart)):
        print('Kevin',len(kevin))
    elif(len(kevin)<len(stuart)):
        print('Stuart',len(stuart))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
