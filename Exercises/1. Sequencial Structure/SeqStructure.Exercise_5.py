#5. Make a program that converts meters to centimeters and centimeter to meters.

i = 1

def main():
    while i == 1:
        try:
            option = int(input('Select what convertion you want to make:\n[1] - Meters -> Centimeters\n[2] - Centimeters -> Meters\n'))
            i_repeat = 1

            while i_repeat == 1:
            #Meters to Centimeters:
                if option == 1:
                    measure = float(input('Type the measure in meters: '))
                    print(f'{measure} meter(s) = {measure*100} centimeter(s)\n')
                
                    i_repeat = 2
                    while i_repeat == 2:
                        repeat = input('Do you want to convert another measure?\n[y] - Yes\n[n] - No\n')
                        if repeat == 'y':
                            i_repeat = 0

                        elif repeat == 'n':
                            exit()

                        else:
                            print('Input Error, try again.\n')
                            i_repeat = 2
                
                #Centimeters to Meters:
                elif option == 2:
                    measure = float(input('Type the measure in centimeters: '))
                    print(f'{measure} centimeter(s) = {measure/100} meter(s)\n')
                
                    i_repeat = 2
                    while i_repeat == 2:
                        repeat = input('Do you want to convert another measure?\n[y] - Yes\n[n] - No\n')
                        if repeat == 'y':
                            i_repeat = 0

                        elif repeat == 'n':
                            exit()

                        else:
                            print('Input Error, try again.\n')
                            i_repeat = 2

                else:
                    print('Type a valid option\n')

        except ValueError:
            print('Input error, try again.\n')
            
main()
            

