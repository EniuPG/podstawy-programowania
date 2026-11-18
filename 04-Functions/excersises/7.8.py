# Minimum coins

def f(amount_to_pay):  # funkcja licząca monety

    coins = 0  # licznik monet

    coins += amount_to_pay // 5  # monety 5 PLN

    amount_to_pay %= 5  # reszta

    coins += amount_to_pay // 2  # monety 2 PLN

    amount_to_pay %= 2  # reszta

    coins += amount_to_pay  # monety 1 PLN

    return coins  # wynik

def main():

    print(f(23))  # 6

    print(f(8))  # 3

    print(f(2))  # 1

    print(f(0))  # 0

if __name__ == "__main__":

    main()