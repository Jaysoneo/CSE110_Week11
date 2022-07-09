people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
ages=[]
names=[]
for person in people:
    line=person.split(' ')
    ages.append(float(line[1]))
    names.append(line[0])

min=ages[0]
for i in range(len(ages)):
    if min > ages[i]:
        min=ages[i]
        youngest=names[i]

max=ages[0]
for i in range(len(ages)):
    if max<ages[i]:
        max=ages[i]
        oldest=names[i]
print(f"""
==================================================================
    The youngest person is {youngest} with {min} years old, and
    the oldest person is {oldest} with {max} years old.
==================================================================""")
