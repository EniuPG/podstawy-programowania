# PIN verification

correct_pin = "0805"  # poprawny PIN

attempts = 0  # licznik prób

while attempts < 3:  # maksymalnie 3 próby

    pin = input("Enter the PIN code: ")  # pobranie PIN-u

    if pin == correct_pin:  # sprawdzenie poprawności

        print("Correct PIN")  # komunikat sukcesu

        break  # zakończenie pętli

    else:  # błędny PIN

        print("Incorrect...")  # komunikat błędu

        attempts += 1  # zwiększenie liczby prób

if attempts == 3:  # po trzech błędnych próbach

    print("Sorry, your payment card has been blocked.")  # blokada karty