print('> Simple Unit Conversion Calculator')
print('> Choose a unit to convert:')

print(' ')

print('> Inch')
print('> Foot')
print('> Yard')
print('> Mile')

print(' ')

starting_unit = input('> Enter a unit of measurement: ')
converting_to = input('> Converting to: ')

print(' ')

number_1 = int(input('> Enter your number: '))

inch_to_foot = number_1 / 12
inch_to_yard = number_1 / 12 / 3

if starting_unit == 'Inch' or 'inch' and converting_to == 'Foot' or 'foot':
    print(inch_to_foot)
if starting_unit == 'Inch' or 'inch' and converting_to == 'Yard' or 'yard':
    print(inch_to_yard)


#print(' ')

#print('> Ounce')
#print('> Pound')
#print('> Kilogram')

#print(' ')

#print('> Fluid Ounce')
#print('> Cup')
#print('> Quart')
#print('> Gallon')

#print(' ')

#print('> Celsius')
#print('> Fahrenheit')