text = 'Wir haben ein langen Text'

'''
der Benutzer soll einen Suchstring eingeben 
und als Antwort erhalten ob der string im Text enthalten ist
GROSS/kleinschreibung soll ignoriert werden

zusatz: leading und trailing spaces 
sollen ignoriert werden (fkt suchen)
'''

print(text)
search = input('Suche: ')
if search.strip().lower() in text.lower():
    print("gefunden")
else:    
    print("nicht gefunden")    
