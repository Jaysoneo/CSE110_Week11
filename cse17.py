print('hello, what is your name?')
name=input('write your name: ')
name=name.capitalize()
print('to read better, the text is displayed in sections, so you have to press enter to continue with the story')
a=input()
print(f"""welcome {name},today is a beautiful day; it is morning, and there are no clouds in the sky.
 In this world you are a 13 years old and the youngest child in a family that lives in the country side.
""")
a=input()
leg=''
#---------------------------------------option1-----------------------------------------------------
print("""Your family owns a farm, and THERE is home. Also, there is a river and a forest near.
Now is the moment to explore, where do you go?""")
a=input()
option_1=input('>go to HOME, RIVER, or FOREST: ')
option_1=option_1.lower()
while option_1!='home' and option_1!='forest' and option_1!='river':
    print('error, you wrote wrong or you choose other option')
    option_1=input('> go to HOME, RIVER, or FOREST: ')
    option_1=option_1.lower()
#               ---------------------op1-----Home---------------------------------
if option_1=='home':
    print('then, you go home')
    a=input()
    print('your house is a big two floors house; the house is big because you have a lot of siblings ')
    a=input()
    print('You enter in the house and there is your mom; according to her look, seems like you are in trouble')
    a=input()
    print(f'mom: where were you {name}? I need your help!')
    a=input()
    print('mom: please cut some logs for the fire and quick!')
    a=input()
    print('You have no options, so you pick an axe and cut some logs')
    a=input()
    print('man, these logs are hard, but they are not a rival for you and your axe!')
    a=input()
    print('after a while you are done, but your mom is here again,so you prepare yourself for the next task')
    a=input()
    print(f'mom: {name} please go to the forest and tell to your brother to comeback home?')
    a=input()
    print('again your future is decided, but now you have more freedom  in this task, so you start your journey')
    a=input()
    print('you are in the forest, and you start to look for your brother, in the distance you hear a sound')
    a=input()
    print('there is only one person in this forest, so it has to be your brother')
    a=input()
    print('you hear closer and colser the sound until you see what is the cause of the sounds')
    a=input()
    print('...')
    a=input()
    print('the sound was a wolf')
    a=input()

    option_2=input('>RUN, CLIMB a tree, FIGHT: ')
    option_2=option_2.lower()
    while option_2!='run'and option_2!='climb'and option_2!='fight':
        option_2=input('>That was wrong, quick! RUN, CLIMB a tree, FIGHT: ')
        option_2=option_2.lower()

    if option_2=='run':
        print("""Whithout thinking your legs start to move. You have never run as fast as today.
You can feel your heart beating in your chest and the sound of bushes behind you""")
        a=input()
        print('wolf is behind you and it is faster than you, you don\'t have more option than hide or fight')
        option_3=input('>RUN, CLIMB a tree, FIGHT: ')
        option_3=option_3.lower()

        while option_3!='run'and option_3!='climb'and option_3!='fight':
            option_3=input('>The wolf is about to eat you!, RUN, CLIMB a tree, FIGHT: ')
            option_3=option_3.lower()
        
        if option_3=='run':
            print('running is useless, the wolf is faster than you')
            option_3=input('RUN anyway, CLIMB a tree, or FIGHT: ')
            option_3=option_3.lower()
            while option_3!='run'and option_3!='climb'and option_3!='fight':
                option_3=input('>The wolf is about to eat you!, RUN, CLIMB a tree, FIGHT: ')
                option_3=option_3.lower()

            if option_3=='run':
                print('you run and the wolf bites your leg')
                a=input()
                print('you fall down and the wolf is about to bites you again')
                a=input()
                option_4=input('HELP or FIGHT: ')
                option_4=option_4.lower()
                while option_4!='help'and option_4!='fight':
                    option_4=input('>The wolf is about to eat you!, RUN, CLIMB a tree, FIGHT: ')
                    option_4=option_4.lower()
                if option_4=='help':
                    print('You scream for help')
                    a=input()
                    print('but nobody came')
                    a=input()
                    print('the wolf attacks you, but you defend yourself with your arm')
                    a=input()
                    print('sunddenly, the wolf stop atacking you')
                    a=input()
                    print('the wolf is bleeding, then, you realize that you just have awaken your powers')
                    a=input()
                    print('then you realize that your oldest brother is there, and that you don\'t have powers')
                    a=input()
                    print('your oldest brother kill the wolf with his axe, and now you are safe')
                if option_4=='fight':
                    option_3='fight'
                    leg='hurt'
            if option_3=='climb':
                option_2='climb'
            if option_3=='fight':
                option_2='fight'
        if option_3=='climb':
            option_2='climb'
        if option_3=='fight':
            option_2='fight'
    if option_2=='climb':
        print("""Using all of your strength, you climb the closest tree, then,
you hear the wolf trying to climb the tree.""")
        a=input()
        print('you are safe here, but the wolf in waiting for you in the ground')
        a=input()
        print('...')
        a=input()
        print('the only thing you can do is to wait here')
        a=input()
        print('then, you remember that your brother is in the forest too, so you scream')
        option_3=input('scream HELP wolf! or RUN wolf!: ')
        option_3=option_3.lower()
        while option_3!='help' and option_3!='run':
            option_3=input('what do you scream? HELP wolf or RUN wolf!: ')
            option_3=option_3.lower()
        a=input()
        print(f'you scream {option_3}')
        a=input()
        print('you see that the sky is orange, and you start to worry about if this tree is going to be your new house')
        a=input()
        if option_3=='help':
            print('after a while, you listen some steps and bushes')
            a=input()
            print('Your oldest brother is here, and he is with his axe ready to fight')
            a=input()
            print('the wolf tries to attack your brother, but he cut its hed with his axe')
            a=input()
            print(f'Brother: {name}, now you are safe')
            a=input()
            print('you: mom said that you have to go home!')
            a=input()
            print('you and your brother go home')
        elif option_3=='run':
            print('after a while, you listen some steps and bushes')
            a=input()
            print('Your oldest brother is here, and he is with his axe ready to fight')
            a=input()
            print('the wolf tries to attack your brother, but he cut its hed with his axe')
            a=input()
            print(f'Brother: {name} why are you saying to run when you need help?')
            a=input()
            print('you: u.u')
            a=input()
            print('you: mom said that you have to go home!')
            a=input()
            print('you and your brother go home')

        
    if option_2=='fight':
        print('YOU were able to cut all that wood, a wolf is nothing')
        a=input()
        print('you use all of your strength and you punch the wolf')
        a=input()
        print('the wolf tries to attack you, but you punch it again')
        a=input()
        print('you keep fighting the wolf until the animal flees')
        a=input()
        print('now that you are safe, you can finish your task')
        if leg=='hurt':
            print('your leg is hurted, so rest under a tree ')
            a=input()
            print('you scream the name of your brother while you feel how your adrenaline levels go down')
            a=input()
        else:
            print('you look for your brother, but the forest is big')
            a=input()
            print('you keep walking until you find him')
            a=input()
        print('yor brother is here and you finish your task by saying that he has to go home')
        if leg=='hurt':
            print('Brother: what happened to you, are you hurted?')
            a=input()
            print('you: please go home')
            a=input()
        a=input()
        print('you and your brother go home')

#               ---------------------op1------River-------------------------------
elif option_1=='river':
    print('then, you go to the river')
    a=input()
    print(f"""
The river is not too big, at least 20ft wide, and the speed of water is relatively low. 
Seems like today is a perfect day to swim in the river, """)
    option_2=input('> swim? YES or NO: ')
    option_2=option_2.lower()
    while option_2!='yes' and option_2!='no':
        print('error, you wrote wrong or you choose other option')
        option_2=input('> swim? YES or NO: ')
    if option_2=='yes':
        print('you take off your clothes and you are ready to swim')
    else:
        print('Even though today is the perfect day to swim, you decide to stay away from water.')
    a=input()
    print("""suddenly, a young male is walking toward you. He is your best friend, you two
are so good friends that you are like brother. Actually you two are brothers (literally!).
    """)
    a=input()
    print(f"""\nBrother: Hey {name}! what are you doing here??? mom need your help,
Brother: wait a moment, were you about to swim in the river???
     """)
    a=input()
    answer=input('>say a JOKE, YES,or NO: ')
    answer=answer.lower()
    if answer=='yes' and option_2=='yes':
        print('\n{name}: Yes, I was about to swim until you interrupted me :( ')
        a=input()
        print(f'\nBrother: {name} remember that you don\'t how to swim, and please dress your self')
    elif answer=='yes' and option_2=='no':
        print(f'\n{name}: Yes, I mean today is THE perfect day to swim, right? ;)')
        a=input()
        print(f'\nBrother: I dont know why, but I feel like you are lying to me, anyway')
        a=input()
        print(f'\nBrother:  Remember {name}, you don\'t how to swim')
    elif answer=='no' and option_2=='yes':
        print(f'\n{name}: No, why are you saying that?')
        a=input()
        print(f'\nBrother:  Are you kidding me? Were are your clothes?')
    elif answer=='no' and option_2=='no':
        print(f'\n{name}: Nope, I know that today is perfect to swim, but I am not doing that today.')
        a=input()
        print(f'\nBrother:  Thank you for not swiming, remember that you don\'t how to swim')
    elif answer=='joke' and (option_2=='yes' or option_2=='no'):
        print(f'\n{name}: Hey do you know who is Joe? no? Well how it\'s possible that you don\'t JOE mama!!!')
        a=input()
        print(f'\n{name}: Hahahhahahahahahhahahahahahhahahahahhahahahahahahaha')
        a=input()
        print('\n Brother:  ...')
        a=input()
        print('\n Brother: Just... don\'t forget that you don\'t how to swim')
    print('Your brother have a nice time talking ,then, you two go home.')
#                          ----------op1---forest--------------
elif option_1=='forest':
    print('then, you go to the forest')
    a=input()
    print('you walk and you walk until you are in the forest')
    a=input()
    print('you see your oldest brother who is going to cut some wood')
    option_2=input('GO with him or EXPLORE the forest alone: ')
    option_2=option_2.lower()
    while option_2!='go' and option_2!="explore":
        print('please choose right')
        option_2=input('GO with your brother or EXPLORE the forest alone: ')
        option_2=option_2.lower()
    if option_2=='go':
        print('you go with your brother')
        a=input()
        print(f'Brother: {name} what are you doing here? I thought that mom was looking for you?')
        a=input()
        print('you: well, I wanted to go to the forest with you')
        a=input()
        print('Brother: then, you can go with me, but you will have to help me')
        a=input()
        print('you follow your brother, and you two take turns to cut a tree')
        a=input()
        print('you two work until the afternoon, and then you two go home')    
    elif option_2=='explore':
        a=input()
        print('you explore the forest alone')
        a=input()
        print('you see some interesting rocks,trees, and birds')
        a=input()
        print('after while you are deep into the forest')
        a=input()
        print('yes, you are lost')
        option_3=input('CLIMB a tree or scream for HELP: ')
        option_3=option_3.lower()
        while option_3!='climb' and option_3!="help":
            print('please choose right')
            option_3=input('climb a tree or scream for help: ')
            option_3=option_3.lower()
        if option_3=='climb':
            print('for some reason you climb a tree; if you are lucky, there is a chance to see how to go back')
            a=input()
            print('you climb the tree, but you can only  see trees and more trees')
            a=input('')
            print('luckly you can see where is the end of the forest and you are ready to go')
            a=input()
            print('you goes through the forest until you see the light of the day and the green of the grass')
            a=input('')
            print('you scape from the forest and you go home')
            a=input('')            
        elif option_3=='help':
            print('you scream help! But nobody came')
            a=input('')
            print('you keep screaming until your brother is there')
            a=input('')
            print(f'{name}, do you need help?')
            a=input('')
            print('you say yes, and your brother and you go back home')
            a=input('')
#---------------------------------------------------------------------------------------------------------
print('to play the full story, with MORE CONTENT, and even GRAPHICS , the full game is available only for $30,000 ')