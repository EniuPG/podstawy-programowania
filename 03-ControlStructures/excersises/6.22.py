# Numbers from 1 to 30

for i in range(1, 31):  # liczby od 1 do 30

    if i % 3 == 0 and i % 5 == 0:  # podzielne przez 3 i 5
        print("BINGO", end=" ")

    elif i % 3 == 0:  # podzielne przez 3
        print("THREE", end=" ")

    elif i % 5 == 0:  # podzielne przez 5
        print("FIVE", end=" ")

    else:  # pozostałe liczby
        print(i, end=" ")