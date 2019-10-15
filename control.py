'''
this program demonstrates the syntax of the 
if statement
'''

# month_per_year = 12 
a = 12
b = 14


if a < b:
    print('a kleiner b!')   
    print('Ende des IFs')
elif a > b:
    print('a groesser b!')   
else:      
    print('gleich') 
    a = b    
    
print('Ende')    
