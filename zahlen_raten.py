'''
zahlen raten:
+ zufallszahl zw 1-100
+ user darf 5 mal raten
+ info ob zu hoch oder zu nieder
'''

'''
zahlen raten:
+ zufallszahl zw 1-100
+ user darf 5 mal raten
+ info ob zu hoch oder zu nieder
'''

from random import randint

# import only system from os 
from os import system, name 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

clear()

print('Willkommen zum Zahlenraten-Spiel.\nErrate meine Zahl zwischen 1 und 100. Du darfst 5 mal raten.\n')

play_again = True

while play_again:

    number_to_guess = (randint(1, 100))
    won = False
    #print(number_to_guess)
    
    print("Ich habe mir eine Zahl ausgesucht. Los geht's!")

    for i in range(1, 6):

        user_input = int(input(str(i) + '. Versuch: '))
       
        if user_input == number_to_guess:
            print('Gratuliere! Du hast meine Zahl in {:d} Zügen erraten.'.format(i))
            won = True
            break
        elif user_input > number_to_guess:
            print('Deine Zahl ist zu hoch.')
        else:
            print('Deine Zahl ist zu niedrig.')

    if not won:
        print('\nSchade, Du hast meine Zahl nicht erraten! Ich habe mir die Zahl {:d} ausgesucht.'.format(number_to_guess))

    user_input = input('\nMöchtest Du nochmal spielen? (j/n): ')
    if user_input.lower() == 'n':
        play_again = False