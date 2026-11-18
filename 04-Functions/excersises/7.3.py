# Test month function

from month_module import month  # import funkcji

def main():  # funkcja główna

    number = int(input("Enter month number: "))  # pobranie numeru

    print(f"The name of month {number} is {month(number)}")  # wynik

if __name__ == "__main__":  # uruchomienie programu

    main()  # wywołanie funkcji