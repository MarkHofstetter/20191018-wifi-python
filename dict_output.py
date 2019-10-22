h = { 4: 7,
      5: 2,
      2: 8,
      6: 1,
     12: 2,
    }
    
for k in h:
    print(k, h[k])
    
print('****')    

for k,v in h.items():
    print(k, v)
    
print('****')    
    
h_keys = list(h.keys())    
h_keys.sort()
for k in h_keys:
    print(k, h[k])

print('**** nach Häufigkeit sortieren ')        

h_rev = {}
# key und value vertauschen, funktioniert NUR
# wenn die Values auch eindeutig sind!!!
for k,v in h.items():
    h_rev[v] = k

h_rev_keys = list(h_rev.keys())
h_rev_keys.sort()
for k in h_rev_keys:
    print(k, h_rev[k])

print('**** nach Häufigkeit sortieren korrekt')            

from collections import OrderedDict

h_sorted_by_val = OrderedDict(sorted(h.items(), key = lambda x: x[1]))
for k,v in h_sorted_by_val.items():
    print(k, v)

    
print('**** nach Häufigkeit manuell')
from pprint import pprint
'''
teilnehmer = [
        ['Magdalena', 1982],
        ['Herbert', 1973],
        ['Tobias', 1984],
        ['Clemens', 1989],
        ['Sarah', 1994],
        ['Elias', 1997],
        ['Zsolt', 1988],
        ['Birgit', 1987],
        ['Lorenz', 1987],     
    ]

teilnehmer.sort()

pprint(teilnehmer)
'''

# h_as_list = [ list(h.values()), list(h.keys()) ]
h_as_list = []
for k,v in h.items():
    h_as_list.append([v,k])

h_as_list.sort()
pprint(h_as_list)