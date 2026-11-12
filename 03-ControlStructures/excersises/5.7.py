# Countdown timer

seconds = int(input("Enter number of seconds: "))  # pobranie liczby sekund

while seconds > 0:  # dopóki licznik jest większy od zera

    if seconds == 5:  # gdy zostało 5 sekund
        print("five")  # słowny zapis

    elif seconds == 4:  # gdy zostały 4 sekundy
        print("four")  # słowny zapis

    elif seconds == 3:  # gdy zostały 3 sekundy
        print("three")  # słowny zapis

    elif seconds == 2:  # gdy zostały 2 sekundy
        print("two")  # słowny zapis

    elif seconds == 1:  # gdy została 1 sekunda
        print("one")  # słowny zapis

    else:  # dla pozostałych wartości
        print(seconds)  # wyświetlenie liczby

    seconds -= 1  # zmniejszenie licznika

print("Time's up!")  # zakończenie odliczania