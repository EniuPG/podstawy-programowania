# Checking if discount is available
# The discount is available to children under 18
# or people 65 or older

age = int(input("Enter your age: "))  # pobranie wieku

if age < 18 or age >= 65:  # sprawdzenie warunku zniżki
    print("Discount available")  # informacja o zniżce
else:  # jeśli warunek nie został spełniony
    print("No discount")  # brak zniżki