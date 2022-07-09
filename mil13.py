
def farenheit_from_celcius(degrees):
    'input the temperature in celcius degrees and it is converted into farenheit degrees'
    y=(9/5)*degrees+32
    return y
def celcius_from_farenheit(degrees):
    'input the temperature in farenheit degrees and it is converted into celcius degrees'
    y=(degrees-32)*(5/9)
    return y
def mph_to_kmh(v):
    'input a mph speed,then, it is converted into km per hour sppeed'
    y=v*(1.609)
    return y

def wind_chill(wind,temperature):
    'input the wind and the temperature, then, it is calculated the wind chill'
    y=35.74+0.6215*temperature-35.75*(wind**0.16)+0.4275*temperature*(wind**(0.16))
    return y

print("""───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")

temperature=input('\nwhat is the temperature? ')
type_of_temperature=input('farenheit or celcius (F/C)? ')
results=input('do you want the results in farenheit or celcius (F/C)? ')
temperature=float(temperature)
if type_of_temperature.lower()=='c' or type_of_temperature.lower()=='celcius':
    temperature=farenheit_from_celcius(temperature)
if results.lower()=='f' or results.lower()=='farenheit':
    for i in range(5,65,5):
        win_chill=wind_chill(i,temperature)
        print(f'At temperature {temperature}F, and wind speed {i} mph, the windchill is: {win_chill:.2f}F')
elif results.lower()=='c' or results.lower()=='celcius':
    temperature=celcius_from_farenheit(temperature)
    for i in range(5,65,5):
        win_chill=wind_chill(i,temperature)
        print(f'At temperature {temperature:.2f}C, and wind speed {mph_to_kmh(i):.2f} km/h, the windchill is: {win_chill:.2f}C')