'''
beliebige Anzahl Zahlen vom User lesen (bis 0)
in eine Liste geben

am ende alle Zahlen der Liste summieren 
Summe und Liste ausgeben

zusatz: die 0 sollte nicht am Ende der Liste stehen
'''

a = [] 

user_input = 1
while True:
    user_input = int(input('Zahl: '))
    if user_input == 0:
        break
    a.append(user_input)

# del(a[-1]) 
print(a)  
sum = 0  
for s in a:
    sum += s

print(sum)    
