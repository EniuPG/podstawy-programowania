# Checks whether at least one number entered
# from the keyboard is not negative

x = int(input("Enter first number: ")) # pobranie pierwszej liczby
y = int(input("Enter second number: ")) # pobranie drugiej liczby

if not x < 0 or not y < 0: # sprawdzenie czy przynajmniej jedna liczba nie jest ujemna
    print(f"At least one of the numbers {x} and {y} is not negative") # wyświetlenie komunikatu
else:
    print(f"Both numbers {x} and {y} are negative") # wyświetlenie komunikatu