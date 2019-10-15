wort  = "irgendwas"
wort2 = "nochwas"

laenge = len(wort)

print("Das Wort {:s} ist {:d} Zeichen lang".format(wort, laenge))

print(wort + ' ' + wort2)
satz = "{:s} {:s}".format(wort, wort2)
print(satz)
print('=' * len(satz))

print(wort.upper())

print('HALLO'.lower())

print(wort.replace('was', 'wie'))

if 'was' in wort:
    print('"was" ist enthalten')

