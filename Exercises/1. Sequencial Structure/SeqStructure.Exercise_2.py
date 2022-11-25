#2. Make a program that ask for a number and then show the message ''The number informed was [number]''.

i = 1

while i == 1:
    number = input('Type a number: ')
    
    if number.isdecimal() == True:
        print(f'The number informed was {number}')
        i = 0
    
    else:
        print('Error! Type a valid number.\n')
