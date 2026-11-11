# Program obliczający liczbę liter pomiędzy dwiema literami

first = input("Enter first letter: ")   # Pierwsza litera

last = input("Enter last letter: ")     # Druga litera

first_letter_code = ord(first)          # Kod pierwszej litery

last_letter_code = ord(last)            # Kod drugiej litery

number_of_letters = abs(last_letter_code - first_letter_code) - 1  # Litery pomiędzy

print(f"Between {first} and {last} is {number_of_letters} letters")  # Wynik