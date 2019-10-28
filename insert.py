import sqlite3

conn = sqlite3.connect('students.db')

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
befüllen der Tabelle mit den Daten (name und yob) 
aus dem dictionary
'''

for name, data in teilnehmer.items():
    birth_year = data['yob']
    print(name, birth_year)    
    conn.execute("insert into student(name, birth_year) values (?,?)", 
        (name, birth_year))

conn.commit()


