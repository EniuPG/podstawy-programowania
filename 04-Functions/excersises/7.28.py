# Finds value occurring most times in a row

def f(dice):  # definicja funkcji

    max_count = 1  # maksymalna długość serii

    current_count = 1  # aktualna długość serii

    result = dice[0]  # wynik

    for i in range(1, len(dice)):  # przejście po ciągu

        if dice[i] == dice[i - 1]:  # ten sam znak

            current_count += 1  # zwiększenie serii

            if current_count > max_count:  # nowy rekord

                max_count = current_count  # zapis długości

                result = dice[i]  # zapis liczby

        else:  # inna liczba

            current_count = 1  # reset licznika

    return int(result)  # zwrócenie wyniku

print(f("5233165554211"))  # 5

print(f("2133"))  # 3