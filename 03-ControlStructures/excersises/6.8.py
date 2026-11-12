# Checking if both people are adults

person1_name = input("Enter first person name: ")  # pobranie pierwszego imienia
person1_age = int(input("Enter first person age: "))  # pobranie pierwszego wieku

person2_name = input("Enter second person name: ")  # pobranie drugiego imienia
person2_age = int(input("Enter second person age: "))  # pobranie drugiego wieku

if person1_age >= 18 and person2_age >= 18:  # sprawdzenie pełnoletności obu osób

    print(f"Both {person1_name} and {person2_name} are adults")  # komunikat sukcesu

else:  # jeśli jedna z osób jest niepełnoletnia

    print(f"Either {person1_name} or {person2_name} is not an adult")  # komunikat