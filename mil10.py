item=''
price=''
quantity=''
list_of_prices=[]
list_of_items=[]
list_of_multiples=[]
#---------------------------------------------Functions-------------------------------------------------
def ident(x,w):
    y=len(x)-len(w)
    z=''
    for i in range(y-1):
        z=z+' '
    return(z)

def longest(x1,t1):
    y1=len(x1[0])
    z1=''
    for i in range(t1):
        if y1<len(x1[i]):
            y1=len(x1[i])
            z1=x1[i]
    return(z1)

#--------------------------------------Here is the start of the program--------------------------------------------------------

print("""\nPlease select one of the folowing:
1. Add item
2. View cart
3. Remove Item
4. Compute total
5. quit
""")
option=input('\nPlease enter an action: ')
while option!='5':



#inputs--------------------------------------------------------------------------------------------   
    if option=='1':
        print("\n===========================================================================================")
        item=''
        print('\nwrite your items and their price, write \"end\" to finish\n')
        while item != 'end':
            item=input('What item would you like to add? ')
            if item!='end':
                price=input(f'What is the price of {item}? $')
                quantity=input('How many of them? (please introduce a number): ')
                if quantity!='1':
                    list_of_multiples.append(quantity)
                else:
                    list_of_multiples.append('1')
                print(f'{item} has been added to the cart')
                list_of_items.append(item)
                list_of_prices.append(price)
        print("===========================================================================================")
        continu=input('\npress enter to go back to the main menu\n  ')




#printing the list -------------------------------------------------------------------------------
    elif option == '2':
        n=int(len(list_of_items))
        print("\n===========================================================================================")
        print('\nThe contents of the shopping car are:\n ')
        if list_of_items==[]:
            print('the cart is empty')
        else:
            long_word=longest(list_of_items,n)
            longest_number=longest(list_of_multiples,n)
            for i in range(n):
                if long_word!=list_of_items[i]:
                    space=ident(long_word,list_of_items[i])
                    space2=ident(longest_number,list_of_multiples[i])
                    print(f"""{i+1}.  x{list_of_multiples[i]} {list_of_items[i]} {space} {space2}--- ${list_of_prices[i]}""")
                else:
                    print(f"""{i+1}.  x{list_of_multiples[i]}  {list_of_items[i]} --- ${list_of_prices[i]}""")        
        print("===========================================================================================")

        continu=input('\npress enter to go back to the main menu  ')



#remove ---------------------------------------------------------------------------------------
    elif option=='3':
        print("\n===========================================================================================")
        remove=input('\nwhich item would you like to remove?(write its number): ')
        n=len(list_of_items)
        i=0
        while i!=n:
            if remove!=str(i+1):
                number=False
                i=i+1
            elif remove==str(i+1):
                number= True
                i=n
            else:
                i=n

        if n==0:
            number=True

        while  not number :
            print('\n ERROR: you didn\'t write a valid number')
            remove=input('\n which item would you like to remove? (please write its number): ')
            number=False
            i=0
            while number==False:
                if remove == str(i+1):
                    number= True
                else:
                    number= False
                i=i+1
        if n==0:
            print('the cart is empty')
        else:
            remove=int(remove)-1
            list_of_prices.pop(remove)
            removed_item=list_of_items.pop(remove)
            list_of_multiples.pop(remove)
            print(f'{removed_item} as been removed\n')
        print("===========================================================================================")
        
        continu=input('\npress enter to go back to the main menu  ')




#total------------------------------------------------------------------------------------------------
    elif option=='4':
        
        total=0
        n=int(len(list_of_prices))
        for i in range(n):
            total=total+float(list_of_prices[i])*float(list_of_multiples[i])
        print("\n===========================================================================================")
        print(f'\nThe total price of the items in the shopping cart is ${total:.2f}\n')
        print("===========================================================================================\n")
        continu=input('press enter to go back to the main menu  ')
    print("""\nPlease select one of the folowing:
1. Add item
2. View cart
3. Remove Item
4. Compute total
5. quit
""")
    option=input('Please enter an action: ')



print('\nthank you for shopping <3')
    