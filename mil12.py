country=[]
code=[]
year=[]
life_exp=[]

with open('life-expectancy.csv') as data:
    for line in data:
        line=line.strip()
        line=line.split(',')
        if line[0]!='Entity':
            country.append(line[0])
            code.append(line[1])
            year.append(line[2])
            life_exp.append(line[3])

#================lowest and biggest life exp and year======================
min=life_exp[0]
for i in range(len(life_exp)):
    if min>life_exp[i]:
        min=life_exp[i]
        low_country=country[i]
        min_year=year[i]

max=life_exp[0]
for i in range(len(life_exp)):
    if max<life_exp[i]:
        max=life_exp[i]
        big_country=country[i]
        max_year=year[i]

print(f'The overall max life expectancy is: {max} from {big_country} in {max_year}')
print(f'The overall min life expectancy is: {min} from {low_country} in {min_year}')

enter=input('press any key to continue ')
#                      =================menu======================
option=''
while option!='5':
    print("""
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    Please select an option
1----find the average life expectancy, minimum, and maximun in a given year.
2----find the maximum and minimum life expectancy given a country.
3----type a country and see its data available.
4----type a year and see the data available at that year.
5----quit.
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
""")
    option=input('write your option number: ')
    while option!='1' and option!='2' and option!='3' and option!='3' and option!='4' and option!='5':
        print('error, invalid character or number')
        option=input('write your option number: ')

#                         ============== option 1 ==================
#                                --------average---------
    if option=='1':
        input_year=input('introduce a year: ')
        indexes=[]
        for i in range(len(country)):
            if year[i]==input_year:
                indexes.append(i)
        average=0
        for i in range(len(indexes)):
            average=float(life_exp[indexes[i]])+average
            n=i
        average=average/(n+1)
#                     -----------------min and max ------------------------
        max=0
        for i in range(len(indexes)):
            j=indexes[i]
            if max<float(life_exp[j]):
                max=float(life_exp[j])
                max_country=country[j]
        min=999
        for i in range(len(indexes)):
            j=indexes[i]
            if min>float(life_exp[j]):
                min=float(life_exp[j])
                min_country=country[j]
        max=float(max)
        min=float(min)

        print(f"""
        During {input_year}: 
        The average life expectancy is {average:.2f} years
        {max_country} had the highest life expectancy with {max:.2f} years, and 
        {min_country} had the lowest life expectancy with {min:.2f} years.
""")
        enter=input('press any key to continue ')
#                         ============== option 2 ==================
    if option=='2':
        super_option=''
        while super_option!='quit':
            country_years=[]
            country_data=[]
            min=999
            max=0
            given_country=input('type the name of a country: ')

            for i in range(len(country)):
                if given_country==country[i]:
                    bug=False
                    break
                else:
                    bug=True
            while bug:
                print('error, invalid country name\n')
                given_country=input('write a country: ')
                for i in range(len(country)):
                    if given_country==country[i]:
                        bug=False
                        break
                    else:
                        bug=True

            for i in range(len(country)):
                if given_country==country[i]:
                    country_years.append(year[i])
                    country_data.append(life_exp[i])
            for i in range(len(country_years)):
                if min>float(country_data[i]):
                    min=float(country_data[i])
                    min_year=country_years[i]
            for i in range(len(country_data)):
                if max<float(country_data[i]):
                    max=float(country_data[i])
                    max_year=country_years[i]

            print(f"""
-----------------------------------------------------------------------------------
In {given_country} the minimum life expectancy was {min} years in {min_year}, and
the maximum life expectancy was {max} years in {max_year}.
-----------------------------------------------------------------------------------
""")
            super_option=input('write \'quit\' to quit or press any key to continue: ')
#                         ============= option 3 ================== 
    elif option=='3':
        given_country=input('type the name of a country: ')
        for i in range(len(country)):
            if given_country==country[i]:
                bug=False
                break
            else:
                bug=True
        while bug:
            print('error, invalid country name\n')
            given_country=input('write a country: ')
            for i in range(len(country)):
                if given_country==country[i]:
                    bug=False
                    break
                else:
                    bug=True
        country_data=[]
        country_years=[]

        for i in range(len(life_exp)):
            if given_country==country[i]:
                country_data.append(life_exp[i])
                country_years.append(year[i])

        print(f'In {given_country} the data available is the following: ')
        for i in range(len(country_years)):
            print(f'year: {country_years[i]}--- life expectancy: {country_data[i]}')
        enter=input('press any key to continue ')
        
#                         ============= option 4 ==================
    elif option=='4':
        country_data=[]
        country_names=[]
        given_year=input('introduce a year: ')
        for i in range(len(year)):
            if given_year==year[i]:
                country_data.append(life_exp[i])
                country_names.append(country[i])
        print(f'during {given_year}: ')
        for i in range(len(country_data)):
            print(f'{country_names[i]}------{country_data[i]} years')
        enter=input('press any key to continue ')