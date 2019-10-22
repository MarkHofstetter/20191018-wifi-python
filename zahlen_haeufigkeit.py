'''
user gibt zahlen ein 0 = Ende
am ende wird ausgegeben (einfahc mit pprint) wie oft eine Zahl 
eingegeben wurde

2
3
4
5
2
2
3

Ausgabe aus pprint(!):

2: 3 
4: 1
5: 1
3: 2
'''

from pprint import pprint

count = {} # count = dict()
while True:
    user_input = input('Bitte Zahl eingeben ')
    if user_input == '0':
        break
    if user_input in count:
        '''
        m = count[user_input]
        m += 1
        count[user_input] = m
        ''' 
        count[user_input] += 1
    else:
        count[user_input] = 1


 
pprint(count)