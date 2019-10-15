# kopfrechen
# der benutzer bekommt 2 unterschiedliche zufallszahlen jeweils im Bereich 1 - 10
# die muss der Benutzer multiplizieren
# und es wird ueberprueft ob die aufgabe richtig geloest wurde

# zusatz
# 10 verschiedene Aufgaben stellen und sich merken 
# wieviel richtig und falsch waren

import random
from util import user_input_positive_number
# import util
    
wrong = 0
right = 0

user_input = user_input_positive_number(question = 'Wieviele Runden')

for i in range(0, user_input):
    print(i)
    m1 = random.randint(1, 10)
    m2 = random.randint(1, 10)

    print(str(m1) + ' mal ' + str(m2) + ' ergibt?')

    product = m1 * m2
    user_input = user_input_positive_number('Bitte eine Lösung eingeben: ')    
    
    if product == user_input:
        print("Richtig!")
        right += 1
    else:
        print("Falsch!")    
        wrong += 1
        
print('Richtig: ' + str(right) )
print('Falsch: ' + str(wrong))
print('Korrekt {:0.2f} %'.format(right/(i+1)*100))


