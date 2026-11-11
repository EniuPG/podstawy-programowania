 #Program obliczający odległość do horyzontu

import math                       # Import funkcji matematycznych

h = float(input("Height in meters: "))  # Wysokość podana przez użytkownika

d = 3.57 * math.sqrt(h)           # Wzór na odległość do horyzontu

print("Distance to horizon:", d, "km")  # Wyświetlenie wyniku

#h = 1.7                           # Wzrost obserwatora
#d = 3.57 * math.sqrt(h)           # Obliczenie odległości

#print(d)                          # Wynik około 4.65 km

##import math

#h = 20                            # Wysokość okna
#d = 3.57 * math.sqrt(h)           # Obliczenie odległości

#print(d)                          # Wynik około 15.96 km
