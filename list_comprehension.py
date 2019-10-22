a = [ 2, 3, 4 ]

'''
ein neue Liste wo jeder wert der Liste a um 1 erhöht ist
'''

# b = []
# b = list()
# for i in a:
#     b.append(i+1)

a = [x+1 for x in a]
    
print([i+1 for i in a])    

l = [3.4, 5.6, 5.9]
l = [ int(x) for x in l ]
print(l)

lotto = [ x for x in range(1, 46) ]
print(lotto)

d = [2] * 10
print(d)

