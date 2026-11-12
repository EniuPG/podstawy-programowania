# Program that simulates the operation of an electronic thermometer

temperature = int(input("Enter temperature: "))  # pobranie temperatury

if temperature > 35:  # temperatura powyżej 35
    print("It is extremely hot")  # komunikat

elif temperature > 30:  # temperatura powyżej 30
    print("It is hot")  # komunikat

elif temperature >= 15:  # temperatura od 15 do 30
    print("It is warm")  # komunikat

elif temperature >= 0:  # temperatura od 0 do 14
    print("It is cold")  # komunikat

else:  # temperatura poniżej 0
    print("Warning, frost")  # ostrzeżenie