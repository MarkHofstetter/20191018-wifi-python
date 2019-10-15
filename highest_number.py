# vom Benutzer Zahlen abfragen bis er/sie 0 eingibt
# dann die höchste Zahl ausgeben

# die initiale max Zahl auf einen möglichst kleinen wert setzen
max = None
user_input = 1

# mach weiter solange der Benutzer nicht 0 eingibt
while user_input != 0:
    # frag den Benutzer nach einer Zahl
    user_input = int(input('Zahl: '))
    # ist der user input größer als die bisherige maximale zahl?
    if max is None or user_input > max:
        max = user_input
   
print("Höchste Zahle {:d}".format(max))        