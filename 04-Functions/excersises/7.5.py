from range_untils import in_range  # import funkcji

def main():

    number = 7  # testowana liczba

    result = in_range(number, 2, 15)  # sprawdzenie zakresu

    print(f"Number {number} in range <2,15>: {'yes' if result else 'no'}")

if __name__ == "__main__":

    main()