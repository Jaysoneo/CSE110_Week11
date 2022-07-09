bank_account=[]
balances=[]

name=''
ba=''
while name!='quit':
    name=input('type the name of your bank account: ')
    if name!='quit':
        ba=input(f'type the balance of {name}: ')
        bank_account.append(name)
        balances.append(ba)
#printing----------------------------------
print('Account info:')
for i in range(len(bank_account)):
    print(f'{i}. {bank_account[i]}----------{balances[i]}')
#loop------------------------------------------------------------
ans=input('do you want to update an account?')
while ans!='no':
    m=int(input('what is the index of your account'))
    ba=input(f'waht is the new amount of {bank_account[m]}')
    balances[m]=ba
    print('\nAccount info:')
    for i in range(len(bank_account)):
        print(f'{i}. {bank_account[i]}----------{balances[i]}')
    ans=input('do you want to update an account?')
total=0
average=0

for i in range(len(bank_account)):
    total=float(balances[i])+total
average=total/len(bank_account)

max=balances[0]
n=0
for i in range(len(balances)):
    if max<balances[i]:
        max=balances[i]
        n=i

print(f"""the total of your bank accounts is: ${total}
the average is: ${average}
max: {bank_account[n]}""")
