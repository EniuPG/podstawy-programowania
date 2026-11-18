# Binary checker

def f(binary_number):  # funkcja sprawdzająca

    for digit in binary_number:  # sprawdzanie każdego znaku

        if digit not in "01":  # jeśli znak nie jest 0 lub 1

            return False  # liczba nie jest binarna

    return True  # poprawna liczba binarna

def main():

    print(f("101101"))  # True

    print(f("1311a10100"))  # False

if __name__ == "__main__":

    main()