# Calculates triangle area

import math # potrzebne do pierwiastka

def triangle_area(a, b, c): # definicja funkcji
    p = (a + b + c) / 2 # półobwód

    area = math.sqrt(p * (p - a) * (p - b) * (p - c)) # wzór Herona

    return area # zwrot pola

print("The area of triangle with sides 3,4,5 is", triangle_area(3, 4, 5)) # wynik

print("The area of triangle with sides 5,12,13 is", triangle_area(5, 12, 13)) # wynik

print("The area of triangle with sides 7,24,25 is", triangle_area(7, 24, 25)) # wynik