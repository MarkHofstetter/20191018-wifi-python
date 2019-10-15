# vom Benutzer Wörte abfragen bis er/sie '0' eingibt
# dann das längste Wort (mit Zahl der Buchstaben) ausgeben

max = ''
user_input = max

# mach weiter solange der Benutzer nicht '0' eingibt
while user_input != '0':
    # frag den Benutzer nach einem wort
    user_input = input('Wort: ')    
    if len(user_input) > len(max):
        max = user_input
   
print("Längstes Wort {:s} mit {:d} Buchstaben".format(max, len(max)))        