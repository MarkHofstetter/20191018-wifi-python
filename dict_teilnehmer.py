from pprint import pprint

teilnehmer = {
        'Lydia': {'yob': 1981, 'fav_col': 'grün', 'edu': ['VS', 'Gym', 'Uni']},
        'Magdalena': {'yob': 1982},
        'Herbert': {'yob': 1973},
        'Tobias': {'yob': 1984},
        'Clemens': {'yob': 1989},
        'Sarah' : {'yob': 1994, 'fav_col': 'lila'},
        'Elias': {'yob': 1997},
        'Zsolt': {'yob': 1988},
        'Birgit': {'yob': 1987},
        'Lorenz': {'yob': 1987, 'edu': ['VS', 'HAK', 'wifi']},
        'Mark': {'yob': 1975, 'fav_col': 'blau', 'edu': ['VS', 'Gym', 'Uni']},
    }

'''
geburtsdaten = list(teilnehmer.values())
geburtsdaten.sort()
print(geburtsdaten)
'''

pprint(teilnehmer)

search = input('Namen? ')

'''
dem gewählten Teilnehmer eine Ausbildung hinzufügen 
druch Eingabe
'''

edu = input('(Zusätzliche) Ausbildung? ')
if 'edu' in teilnehmer[search]:
    teilnehmer[search]['edu'].append(edu)
else:
    teilnehmer[search]['edu'] = [edu]

print(teilnehmer[search]['edu'])

try:
    print("{:s} geboren {:d}".format(search, teilnehmer[search]['yob']))
    try:
        print(teilnehmer[search]['fav_col'])
    except KeyError:
        print("Kein Lieblingsfarbe gefunden")   

    if 'edu' in teilnehmer[search]:        
        print(teilnehmer[search]['edu'][-1]) 
            
except KeyError:
    print("Kein Teilnehmer gefunden")   


    
