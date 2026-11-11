# Program zamieniający wartości dwóch zmiennych

x = 7 # Wartość początkowa x
y = 34 # Wartość początkowa y
z = 0 # Zmienna pomocnicza

print("Before swapping: x=", x, "y=", y) # Stan przed zamianą

z = x # Zapisanie wartości x
x = y # Przypisanie y do x
y = z # Przypisanie starego x do y

print("After swapping: x=", x, "y=", y) # Stan po zamianie