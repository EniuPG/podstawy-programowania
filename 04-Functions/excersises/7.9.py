# Sum even or odd digits

def f(number, even):  # funkcja licząca

    total = 0  # suma

    for digit in str(abs(number)):  # przejście po cyfrach

        digit = int(digit)  # zamiana na int

        if even and digit % 2 == 0:  # tylko parzyste

            total += digit

        elif not even and digit % 2 != 0:  # tylko nieparzyste

            total += digit

    return total  # wynik

def main():

    print(f(3124, True))  # 6

    print(f(3124, False))  # 4

    print(f(20576, False))  # 12

    print(f(20576, True))  # 8

    print(f(13115, True))  # 0

if __name__ == "__main__":

    main()