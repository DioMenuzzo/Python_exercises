#4. Make a program that order the 4 bimonthly notes and show the average. 

i = 1

while i == 1:
    try:
        n1 = float(input('Type the score 1: '))
        n2 = float(input('Type the score 2: '))
        n3 = float(input('Type the score 3: '))
        n4 = float(input('Type the score 4: '))

        print(f'\n({n1} + {n2} + {n3} + {n4})/4 = {(n1+n2+n3+n4)/4}')

        i = 0

    except ValueError:
        print('Type a valid number!\n')
