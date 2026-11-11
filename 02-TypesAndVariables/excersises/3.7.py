# Program obliczający populację obu półkul

total = 8000000000                 # Populacja świata
north = 7200000000                 # Populacja półkuli północnej

south = total - north              # Populacja półkuli południowej

print("World population:", total)  # Wyświetlenie populacji świata

print("Northern Hemisphere:", north)               # Liczba mieszkańców północy
print("Northern Hemisphere in %:", north / total * 100)  # Procent północy

print("Southern Hemisphere:", south)               # Liczba mieszkańców południa
print("Southern Hemisphere in %:", south / total * 100)  # Procent południa

#wyniki:
#Northern Hemisphere: 7200000000
#Northern Hemisphere in %: 90.0
#Southern Hemisphere: 800000000
#Southern Hemisphere in %: 10.0