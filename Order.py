list=[1,1,1,1,1,1,1,1,20,1,1,1,1,1,1,1,1,0,0,100,1,1,1,1,1,1,2]
l=int(len(list))-1
aulist=[]
olist=[]
max=-1
n=l+1

for j in range(n):
    for i in range(l):
        n1=i
        n2=i+1
        m1=list[n1]
        if m1>=max:
            max=m1

    for i in range(l):
        if list[i]!= max:
            aulist.append(list[i])
        else:
            for j in range(len(olist)):
                if olist[j]==max:
                    aulist.append(list[i])

    if max!=-1:
        olist.append(max)
    list=aulist
    l=len(list)-1
    aulist=[]
    max=-1
    print(olist)
    print(list)


