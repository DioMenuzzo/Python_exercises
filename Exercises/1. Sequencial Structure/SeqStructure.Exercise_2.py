#2. Faça um Programa que peça um número e então mostre a mensagem ''O número informado foi [número]''. 

i = 1

while i == 1:
    number = input('Type a number: ')
    
    if number.isdecimal() == True:
        print(f'You typed the number {number}')
        i = 0
    
    else:
        print('Error! Type a valid number.\n')