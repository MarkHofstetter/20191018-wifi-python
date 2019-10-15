a = 10
b = input('Divisor: ')

try:
    b = int(b)
    print(a/b)
except ValueError:
    print("ungültiger Wert")
except ZeroDivisionError:
    print("Division durch 0")
except Error:
    print("es ist was passiert")    