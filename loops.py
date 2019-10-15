'''
loops

'''

for i in range(10, 20, 2):
    if i == 12:
        continue
    print(i)    
    if i > 15:
        break

print('Ende')

c = 5
while c > 0:
    print(c)
    c -= 1    # is the same as c = c - 1;
    
# repeat until
c = 0
while True:
    print(c)
    c -= 1
    if c < 0:
        break