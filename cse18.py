names=''
friends=[]
while names != 'end':
    names=input('Type the name of a friend: ')
    if names !='end':
        friends.append(names)
n=int(len(friends))

print('your friends are:\n ')
for i in range(n):
    print(f"""{friends[i]}""")