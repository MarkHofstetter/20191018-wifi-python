import re

'''
eine österreichische PLZ beginnt 
mit einem A (groß oder klein)
dann darf ein - oder ein 
Leerzeichen oder nichts sein
danach genau 4 Ziffern 

+ davon darf die erste nicht 0 werden
+ beliebig viele Whitespaces
(welche Characterclass)

+ 10 Beispiele in eine dictonary
key = plz?
value = True oder False

5 True und 5 False

+ iterieren über dieses dictionary
+ die regex drauf anwenden und ausgabe
wenn der Erwartungswert nicht dem dem Ergebnis 
entspricht


'''

test = { 
    'A1234': True,
    'B1234': False,
    'A-12345': False,
    'A    1234': True,
    'A-0123': False,
    # ...
}

for plz, result in test.items():
    print(plz, result)
    match = re.search(
        r'^[Aa][- ]{0,1}\d{4}$', 
        plz)
        
    if match is None and result is True:
        print("passt NICHT")
    else:
        print("passt")

