# A simple number guessing game

import random  # import modułu losującego

number_to_guess = random.randint(1, 100)  # losowanie liczby od 1 do 100
user_guess = 0  # początkowa wartość zgadywanej liczby

print("Guess the number between 1 and 100!")  # komunikat startowy

while user_guess != number_to_guess:  # dopóki liczba nie zostanie odgadnięta

    user_guess = int(input("Enter your guess: "))  # pobranie liczby od użytkownika

    if user_guess < number_to_guess:  # sprawdzenie czy liczba jest za mała
        print("Too low! Try again.")  # podpowiedź

    elif user_guess > number_to_guess:  # sprawdzenie czy liczba jest za duża
        print("Too high! Try again.")  # podpowiedź

    else:  # poprawna liczba
        print("Congratulations! You guessed the correct number.")  # komunikat wygranej