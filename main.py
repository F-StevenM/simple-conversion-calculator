print('> Simple Unit Conversion Calculator')
print('> Choose a unit to convert:')

print(' ')

print('> Inch')
print('> Foot')
print('> Yard')
print('> Mile')

print(' ')

print('> Enter the units of measurments exactly as they are printed (Case sensitive)')
starting_unit = input('> Enter a unit of measurement: ')
converting_to = input('> Converting to: ')

print(' ')

number_1 = int(input('> Enter your number: '))

# Starting point: Inch
if starting_unit == 'Inch' and converting_to == 'Foot':
    print('Foot/Feet:', number_1 / 12)
if starting_unit == 'Inch' and converting_to == 'Yard':
    print('Yard(s):', number_1 / 12 / 3)
if starting_unit == 'Inch' and converting_to == 'Mile':
    print('Mile(s):', number_1 / 12 / 5280)

# Starting point: Foot
if starting_unit == 'Foot' and converting_to == 'Inch':
    print('Inches:', number_1 * 12)
if starting_unit == 'Foot' and converting_to == 'Yard':
    print('Yard(s):', number_1 / 3)
if starting_unit == 'Foot' and converting_to == 'Mile':
    print('Mile(s):', number_1 / 5280)

# Starting point: Yard
if starting_unit == 'Yard' and converting_to == 'Inch':
    print('Inches:', number_1 * 12)
if starting_unit == 'Yard' and converting_to == 'Foot':
    print('Foot/Feet:', number_1 * 3)
if starting_unit == 'Yard' and converting_to == 'Mile':
    print('Mile(s):', number_1 / 1760)

# Starting point: Mile
if starting_unit == 'Mile' and converting_to == 'Inch':
    print('Inches:', number_1 * 5280 * 12)
if starting_unit == 'Mile' and converting_to == 'Foot':
    print('Foot/Feet:', number_1 * 5280)
if starting_unit == 'Mile' and converting_to == 'Yard':
    print('Yard(s):', number_1 *5280 / 3)