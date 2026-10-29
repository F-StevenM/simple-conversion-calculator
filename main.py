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

if starting_unit == 'Inch' and converting_to == 'Foot':
    print(number_1 / 12)
if starting_unit == 'Inch'and converting_to == 'Yard':
    print(number_1 / 12 / 3)



















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