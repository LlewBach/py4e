minInt = None
maxInt = None

while True:
    num = input('Enter integer: ')
    if num == 'done':
        print('Maximum is ' + str(maxInt))
        print('Minimum is ' + str(minInt))
        break
    
    try:
        integer = int(num)
    except ValueError:
        print('Invalid input')
        continue

    if minInt == None or integer < minInt:
        minInt = integer
    elif maxInt == None or integer > maxInt:
        maxInt = integer