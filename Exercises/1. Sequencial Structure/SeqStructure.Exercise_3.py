#3. Make a program that ask for two numbers and print the sum.

i = 1

while i == 1:
    try:
        n1 = float(input('Type a number: '))
        n2 = float(input('Type another number: '))

        print(f'{n1} + {n2} = {round(n1+n2, 2)}')
        i = 0

    except ValueError:
        print('Error! Type valid numbers.\n')
