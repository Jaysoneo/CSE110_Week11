c1='abcdefghijklmnopqrstuvwxyz'
c2='abcdefghijklmnopqrstuvwxyz '
#option=input('word(w) or number(n)?: ')
option='n'  
while option!='w'and option!='n':
    print('error write again')
    option=input('word(w) or number(n)?: ')
    
if option=='w':
    word=input('write word: ')
    wordout=''
    #key=int(input('write key: '))
    key=0   
    N=int(len(word))
    N2=int(len(c1))
    wn=[]
    for i in range(N):
        for j in range(N2):
            #print(i,j)
            if word[i]==c1[j]:
                wn.append(j)
    ax=0
    for j in range(N2):
        key=j
        #wordout=''
        for i in range(N):
            ax=int(wn[i])+key
            if ax>(N2-1):
                ax=ax-N2
            wordout=wordout+c2[ax]
        wordout=wordout+' '
    print(wordout)
else:
    
    #key=int(input('write key: '))   
    #N=int(input('write lenght: '))
    N=3
    N2=int(len(c1))
    ax=0
    
    wordout=''
    nn=[]

    #for i in range(N):
    #    number=int(input('write number: '))-1
    #    nn.append(number)
    nn=[4,16,19]
        
#DEENCRYPTION OF THE WORD
    k1=0
    k2=0
    k3=0
    for k1 in range (26):
        for k2 in range(26):
            for k3 in range(26):
            #key=k
                #for i in range(N):
                ax1=nn[0]+k1
                ax2=nn[1]+k2
                ax3=nn[2]+k3
                if ax1>25 or ax2>25 or ax3>25:
                    if ax1>25:
                        ax1=ax1-len(c1)
                    elif ax2>25: 
                        ax2=ax2-len(c1)
                    elif ax3>25:
                        ax3=ax3-len(c1)
                    wordout=wordout+c1[ax1]+c1[ax2]+c1[ax3]
                else:
                    wordout=wordout+c1[ax1]+c1[ax2]+c1[ax3]
                wordout=wordout+' '
            print(wordout)
