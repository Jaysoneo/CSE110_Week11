from random import random
from numpy import array

c1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789,.!? '

c3=''
c4=''
c5=''
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
ax1=0
ax2=0
ax3=0
ax4=0
ax5=0
ax6=0
ax7=len(c1)

a=input('decoy(d) or encrypt(e)?: ')

while (a!='d' or a=='e') and (a=='d' or a!='e') :
    print('error')
    a=input('decoy or encrypt?: ')

if a =="d":                    #DECOY
    b1=input('write word: ')
    ax4=len(b1)
    ax6=(input("write key: "))
    for i in range(ax4):
        l3.append(ax6[i])
        for j in range(ax7):       #l5 is the list of the word
            if c1[j]==b1[i]:
                l5.append(j)
    l5=array(l5,int)
    l3=array(l3,int)
    l3=l5-l3

    for i in range(ax4):
        ax5=l3[i]
        while ax5<0:
            ax5=ax5+ax7
        c4=c4+c1[ax5]
    print(c4)
elif a =='e':                  #ENCRYPT
    b=input('write word: ')
    ax1=len(b)
    for j in range(ax1):
        ax2= int(10*random())
        l2.append(ax2)
        #list of the word
        for i in range(ax7):
            if c1[i]==b[j]:
                l4.append(i)
    l6=l2
    l4=array(l4,int)
    l2=array(l2,int)
    l4=l4+l2

    for i in range(ax1):
        ax3=l4[i]
        while ax3>=ax7:
            ax3=ax3-ax7
        #print(ax3)
        c3=c3+c1[ax3]
        c5=c5+str(l2[i])

    print(c3,c5)
