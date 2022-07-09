from numpy import array 
name=[]
id=[]
title=[]
salary=[]

with open('hr_system.txt') as data:
    for line in data:
        line=line.strip()
        info=line.split()
        name.append(info[0])
        id.append(info[1])
        title.append(info[2])
        salary.append(info[3])
salary=array(salary,float)
salary=salary/24
for i in range(len(title)):
    if title[i]=='Engineer':
        salary[i]=salary[i]+1000

for i in range(len(name)):
    print(f'name= {name[i]} ({id[i]}), title= {title[i]} - ${salary[i]:.2f} ')
