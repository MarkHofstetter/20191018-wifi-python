import configparser
from pprint import pprint

config = configparser.ConfigParser()
config.read('woerterbuch.ini')
config.sections()

eng2ger = dict(config['english_to_german'])
how_many_words2translate = int(config['parameter']['how_many_words2translate'])

# ger2eng = {}
# for k,v in eng2ger.items():
#    ger2eng[v] = k
    
ger2eng = dict( (v,k) for k,v in eng2ger.items() ) 
    
# print( ger2eng )

''' 
der user kann ein deutsches oder englisches Wort eingeben
und bekommt die Übersetzung oder eine Fehlermeldung
'''

'''
sooft abfragen wie in der config datei bei 
"how_many_words2translate" steht
dh for schleife
'''

for i in range(how_many_words2translate):
    search = input('Zu übersetzendes Wort: ')
    if search in eng2ger:
        print("Englisch {:s} Deutsch {:s}".format(search, eng2ger[search]))
    elif search in ger2eng:
        print("Deutsch {:s} Englisch {:s}".format(search, ger2eng[search]))
    else:
        print("nichts gefunden")
