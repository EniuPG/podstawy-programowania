# Counts negative even numbers

def f(x, y):  # funkcja licząca

    count = 0  # licznik

    for number in range(x, y + 1):  # liczby z przedziału

        if number < 0 and number % 2 == 0:  # liczba ujemna parzysta

            count += 1  # zwiększenie licznika

    return count  # zwrot wyniku

def main():

    print(f(-7, 8))  # 3

    print(f(-1, 11))  # 0

if __name__ == "__main__":

    main()