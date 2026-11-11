# Program obliczający objętość i pole powierzchni sześcianu

cube_side_string = input("Enter cube side: ")   # Wczytanie długości boku jako tekst

cube_side = int(cube_side_string)               # Zamiana tekstu na liczbę całkowitą

cube_volume = cube_side ** 3                    # Objętość sześcianu a³

cube_surface_area = 6 * cube_side ** 2          # Pole powierzchni 6a²

print(f"The volume of a cube with side {cube_side} is {cube_volume}")  # Wyświetlenie objętości

print(f"The surface area of a cube with side {cube_side} is {cube_surface_area}")  # Wyświetlenie pola