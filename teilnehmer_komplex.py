from pprint import pprint

# name, geburtsjahr, [lieblingsfarbe]

teilnehmer = [
        ['Lydia', 1981, 'grün'],
        ['Magdalena', 1982],
        ['Herbert', 1973],
        ['Tobias', 1984],
        ['Clemens', 1989],
        ['Sarah', 1994],
        ['Elias', 1997],
        ['Zsolt', 1988],
        ['Birgit', 1987],
        ['Lorenz', 1987],
        ('Mark', 1975, 'blau' , ['VS', 'Gym', 'Uni']),
    ]

# teilnehmer.sort()

# print(teilnehmer)
# pprint(teilnehmer)
'''
wir lesen eine usereingabe (name) und durchsuchen die Liste nach dem
Namen und geben entweder das Geburtsjahr oder einen Fehlermeldung aus

zusatz: wenn vorhanden die Lieblingsfarbe
    + über die Länge der Liste
    + more pythonic über die exception
'''
search = input('Namen? ')
found = False

for (i, tn) in enumerate(teilnehmer):
    if search == tn[0]:
        print("{:-05d} {:s} geboren {:d}".format(i, tn[0], tn[1]))
        found = True        
        try:
            print(tn[2])
        except IndexError:
            print('keine Lieblingsfarbe definiert')
            
        try:
            print(tn[3])
            print(tn[3][-1])
        except IndexError:
            print('keine Ausbildung definiert')
        
        
if not found:
    print('nicht u niemand gefunden')


  