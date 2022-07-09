#input--------------------------------------------------------------
print('\nEnter a list of numbers, type stop when finished.\n')
n=0
list=[] 
while n!='stop':
    n=input('> Enter number: ')
    list.append(n)

for i in range(len(list)-1):
    list[i]=float(list[i])
#total--------------------------------------------------------------
total=0
for i in range(len(list)-1):
    total= total+list[i]

#average------------------------------------------------------------

mean=0
for i in range(len(list)-1):
    mean=mean+float(list[i])

mean=mean/(float(len(list))-1)

#max-----------------------------------------------------------------
max=list[0]
for i in range(len(list)-1):
    if max<list[i]:
        max=list[i]
#smallest positive number----------------------------------------------------
small=list[0]
for i in range(len(list)-1):
    if int(list[i])>0:
        small=list[i]

for i in range(len(list)-1):
    if small>list[i] and list[i]>0:
        small=list[i]


print(f'mean={mean:.3f} ----------------- max={max}-------------small={small}------ total={total}')

print('sorted numbwerasdfgdawerdgf')
for i in range(len(list)-1):
    print(int(list[i]))