# Age group checker

age = int(input("Enter your age: "))  # pobranie wieku

if age < 13:  # wiek poniżej 13
    print("Child")  # dziecko

elif age <= 19:  # wiek od 13 do 19
    print("Teen")  # nastolatek

elif age <= 64:  # wiek od 20 do 64
    print("Adult")  # dorosły

else:  # wiek 65 lub więcej
    print("Senior")  # senior