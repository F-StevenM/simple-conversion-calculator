print('> Simple Unit Conversion Calculator')
print('> Choose a unit to convert:')

print(' ')

print('> Inch')
print('> Foot')
print('> Yard')
print('> Mile')

print(' ')

print('> Enter the units of measurments exactly as they are printed')
starting_unit = input('> Enter a unit of measurement: ')
converting_to = input('> Converting to: ')

print(' ')

number_1 = int(input('> Enter your number: '))

# Starting point
if starting_unit == 'Inch' and converting_to == 'Foot':
    print('Foot/Feet:', number_1 / 12)
if starting_unit == 'Inch' and converting_to == 'Yard':
    print('Yard(s):', number_1 / 12 / 3)
if starting_unit == 'Inch' and converting_to == 'Mile':
    print('Mile(s):', number_1 / 12 / 5280)