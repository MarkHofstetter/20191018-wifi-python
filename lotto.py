'''
Ziehung von Lotto Zahlen

+ 6 zufällige aus 45
+ OHNE doppelte (zurücklegen)

1. mit Listenoperationen
(wirklich nur aus der Menge der verbleibenden Zahlen ziehen
Überlegung: wie skaliert der Algorithmus bei 900000 aus eine Million)

2. mit python funktionen (google)
'''

import random

count = 6
max_number = 45

# start_numbers = [ x for x in range(1, max_number + 1) ]


'''
while len(lotto_numbers) < count:
    zz = random.randint(1, max_number)
    if zz not in lotto_numbers:        
        lotto_numbers.append(zz)        
'''
'''
for j in range(1,1000):
    print(j)
'''    
lotto_numbers = []
start_numbers = list(range(1, max_number + 1))

for i in range(0, count):
    zz = random.randint(0, max_number - i - 1)        
    lotto_numbers.append(start_numbers[zz])        
    del(start_numbers[zz])
    
print(lotto_numbers)

for i in range(20):
    lotto_numbers = random.sample(range(1, max_number + 1), 6)
    lotto_numbers.sort()
    print(lotto_numbers)
