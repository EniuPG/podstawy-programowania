# Numeric keyboard using while

i = 6  # początkowy wiersz

while i >= 0:  # dopóki i jest większe lub równe 0

    j = 1  # pierwsza liczba w kolumnie

    while j <= 3:  # trzy kolumny

        print(i + j, end=" ")  # drukowanie liczby

        j += 1  # następna kolumna

    print()  # nowy wiersz

    i -= 3  # przejście do kolejnego wiersza