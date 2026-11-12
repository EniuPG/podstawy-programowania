# Prints the name of university with an extra space
# between characters

university = "Krakow University of Economics"  # nazwa uczelni
university_expanded = ""  # pusty napis na wynik

for char in university:  # przejście przez każdy znak napisu
    university_expanded = university_expanded + char + " "  # dodanie znaku i spacji

print(university)  # wyświetlenie oryginalnej nazwy
print(university_expanded)  # wyświetlenie nazwy ze spacjami