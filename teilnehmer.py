teilnehmer = [
    'Lydia',
    'Magdalena',
    'Herbert',
    'Tobias',
    'Clemens',
    'Sarah',
    'Elias',
    'Zsolt',
    'Birgit',
    'Lorenz',
    'Mark',
    ]

teilnehmer.sort()

for (i, tn) in enumerate(teilnehmer):
    print("{0:-05d} {1:s}".format(i, tn))
    
search = input('Teilnehmer: ')
if search.strip() in teilnehmer:
    print("{:s} gefunden".format(search))
else:
    print("nicht gefunden")
    
    