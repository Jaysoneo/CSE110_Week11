print('do you want to edit a little bit the story?')
C=input('y for yes and n for no: ')
if C=='y':
    adj1=input('write an adjetive')
    anm=input('write an animal')
    v=input('write a verb')
    xn=input('write an exclamation')
    v2=input('write a verb')
    v3=input('write a verb')
    adj2=input('write an adjetive')
    v4=input('write a verb')
    n=input('write a noun')
    v5=input('write a verb')
    v6=input('write a verb')
else:
    adj1='tinny'        #adjetive of the animal
    anm='penguin'       #animal
    v='blowing'         #verb of the animal
    xn='yikes'          #exclamation
    v2='dance'          #verb of the person
    v3='kiss'           #verb of the animal
    adj2='energetic'    #adjetive of the animal
    v4='gack'           #verb of the animal
    v5='sneezed'        #verb of the family
    n='fridge'          #noun that will be climed
    v6='pet'            #verb of the person

print(f"""
The last week, my family and I were really in trouble. It all started when I saw an
{adj1} {anm} {v} up the hallway."{xn.capitalize()}!" I yelled, and my family {v5}.In that moment,
all I could think to do was to {v2} over and over. Suddently, another {adj2} {anm} 
started to {v4}, so I have no other option that climb a {n}. When a person has adrenaline,
they take questionable desitions; that is the reason of why I {v6} the {anm}. Miraculously,
that caused it to stop, but not before it tried to {v3} me right in front of my family.
""")