#print('Hello? Are you there? Who are you?')
#name=input("write your NAME: ")
name='character'
print(f"""welcome {name.capitalize()}, you are 12 years old and the youngest child in family that owns a farm. 
Your mom told you to that she needs wood, but you are a little bit tired, so what do you do?\n""")

option1=input("""you PICK TWIGS in the forest because is the easiest option,
you PICK AN AXE and go to cut some wood because your family needs you, or
you CALL A SYBLING to help you with this impossible task.\n""")

option1=option1.lower()

#Warnings if option 1 is different

if option1=='pick twigs' and option1=='pick and axe' and option1=='call a sybling':
    print('WARNING: you write your option wrong or you did something different to the options\n')
    option1=input('what do you do? PICK TWIGS, PICK AN AXE, or CALL A SYBLING: ')

if option1=='pick twigs' and option1=='pick and axe' and option1=='call a sybling':
    print('WARNING: This is your last chance, choose one of the given options \n')
    option1=input('PICK TWIGS, PICK AN AXE, or CALL A SYBLING: ')
option1=option1.lower()


#options
#forest route
if option1=='pick twigs':
    print('\nyou go for twigs in the forest\n')
    print("""It\'s cold and dark, but it seems like you got enough wood for your family.
    You are returning to your house, but you listen a suspicious sound. What do you do?
    """)
    option1_2=input("""    >throw your wood and RUN to your house,
    >be brave and CHECK the surrounding, or
    >be careful and WALK to your house bringing all of your wood
    """)
    option1_2=option1_2.lower()
#make sure the option is right
    while option1_2!='walk' and option1_2!='check' and option1_2!='run':
        print('choose one of the given options')
        option1_2=input("""    >throw your wood and RUN,
    >CHECK the surrounding, or
    >WALK to your house
    """)

    if option1_2=='run':
        print('you run to your house and suddenly a wolf emerge from the darkness and is atacking you\n')
        print('the wolf is faster than you ,and it bits your leg. Run is not an option, you have to FIGHT\n')
    elif option1_2=='check':
        print('you check what\s going on, and you see a wolf. After that, the wolf emerge from the darkness and is atacking you\n')
        print(f'{name.capitalize()} throws their wood, but they pick one twig to hit the wolf\n')
    elif option1_2=='walk':
        print('you walk to your house, but you are uncomfortable due to the sounds arround you. Suddenly the sound is approaching to you\n')
        print('you feel pain in your leg, then, you realize that a wolf bites your leg\n ')
        print(f'{name.capitalize()} throws their wood, but they pick one twig to hit the wolf\n')
    
    print('You know that you are in danger and there is no time, what do you do to stay alive?\n')

    option1_2_1=input(f"""        {name.capitalize()} FIGHTs the wolf,
        {name.capitalize()} CALLs FOR HELP, or
        {name.capitalize()} GIVEs UP let the wolf eats them
        >""")
    option1_2_1.lower()
    #change of variables to use less space
    a='fight' 
    a1='fights'
    b='call for help'
    b1='calls for help'
    c='give up'
    c1='gives up'

    while option1_2_1!=a and option1_2_1!=b and option1_2_1!= c and option1_2_1!=a1 and option1_2_1!=b1 and option1_2_1!= c1:
        print(f'please {name.capitalize()} there is no time! Choose an option\n')
        option1_2_1=input(f"""        >FIGHT
        >CALL FOR HELP
        >GIVE UP
        >""")
        option1_2_1.lower()

    if a:
        print(f"{name.capitalize()} punches the wolf\'s head ,and it realizes that you won\'t be an easy prey\n ")
        print('The wolf runs to the forest and leaves you\n')
    elif b:
            print("""You scream "HELP!!!!!" with all of your energy. Then you listen that someone is approching to your direction
    : is your oldest brother with a shovel.\n""")
            print('Your oldest brother runs toward you and hit the wolf with the shovel. \n')
            print('The wolf dies and you return with your brother to the house')
    elif c:
            print('You give up and the wolf bites your belly\n')
            print('You scream due to the pain, and the wolf bites stronger, then, everything is dark\n')
            print('you realize that you were sleeping\n')
#Idealistic route
elif option1=='pick an axe':
    print('you go were the wood is storaged, and you start cutting wood with your axe\n')
    print('You succesfully cut all the wood required, and you are ready to come back, but you feel like someone is watching you\n')
    print(f'{name.capitalize()} is walking to their house, but they see a wolf runnig toward them\n')
    print('what do you do?')
    option2_1=input(f"""    {name.capitalize()} does the most reasonable option when they FIGHT WITH THEIR AXE ,
    {name.capitalize()} does the most unreasonable option when FIGHT WITH THEIR HANDS?""")
    option2_1.lower()
    if option2_1!='FIGHT WITH THEIR AXE' and option2_1!='FIGHT WITH THEIR HANDS' and option2_1!='FIGHT WITH THEIR HANDS?':
        print('WARNING: you typed wrong or you choose another option')
    if option2_1=='FIGHT WITH THEIR AXE':
        print('you do a precise cut, just like cutting wood,then, the wolf is sleeping forever')
    elif option2_1=='FIGHT WITH THEIR HANDS' or option2_1=='FIGHT WITH THEIR HANDS?':
        print('you throw your axe, and you punch the wolf\'s head. The wolf bites you, but you punch it again.')
        print('the wolf realize that you are not an easy prey, so it escape')

#cooperative route
elif option1=='call a sibling':
    print('you call your brother who is one year older than you to help you')
#easter egg
else:
    print('for some reason you decided to do something else')

