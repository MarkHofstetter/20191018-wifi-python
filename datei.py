from pprint import pprint
import csv
import statistics

with open("daten.csv", "r") as file:
    lines = csv.reader(file, delimiter=',')
    #for line in lines[1:]:
    #    print(line)    
    data = list(lines)
    
for row in data[1:]:
    
    row2float = [ float(x) for x in row[1:]]       
    
    # find the column/index of the max value
    i = row2float.index(max( row2float ) )    
    print("{:35s}: {:6.2f} ({:s}) {:6.2f}"
       .format(
       row[0], 
       max(row2float), 
       data[0][i+1],
       statistics.mean( row2float ) 
       ))
    
    
'''
+ Ausgabe des Brennstoffnamens, mit dem Höchsten Preis 
(das erste Jahr dem höchsten Preis) und dem Durchnittspreis

A: 567 380 
B: 12  10 

+ eine Grafik des Preisverlaufs

'''
# pprint(data)

# data = [line.split(',')  for line in lines]
