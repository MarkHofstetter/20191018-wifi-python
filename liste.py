#    0  1  2  3  4  5  6 
f = [1, 1, 2, 3, 5, 8, 13,]

print(f)
print(f[3])
print(f[-1])

print(f[0:3])  # exklusive des letzen Elements

print(f[3:])

# f[4] = 'Hallo'
# print(f)

print(len(f))
print(f[3], f[5])
d = [f[3], f[5]]

f.append(21)

f.insert(0,0)  # position, wert(e)
print(f)

f.remove(1) # entfernt den ersten Wert aus der Liste! 
print(f)

del(f[0])   # entfernt per index
print(f)
