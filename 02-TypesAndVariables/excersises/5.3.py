# Program obliczający objętość i pole powierzchni prostopadłościanu

a = int(input("a="))    # Wczytanie pierwszego boku

b = int(input("b="))    # Wczytanie drugiego boku

c = int(input("c="))    # Wczytanie trzeciego boku

volume = a * b * c      # Objętość prostopadłościanu

surface_area = 2 * (a*b + a*c + b*c)   # Pole powierzchni

print(f"Volume = {volume}")            # Wyświetlenie objętości

print(f"Surface area = {surface_area}") # Wyświetlenie pola powierzchni