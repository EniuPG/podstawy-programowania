# Sum numbers divisible by 2 and 3 but not by 4

def f(x, y):  # definicja funkcji

    total = 0  # suma

    for number in range(x, y + 1):  # zakres liczb

        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:  # warunek

            total += number  # dodanie do sumy

    return total  # zwrócenie wyniku

print(f(1, 20))  # 24

print(f(10, 30))  # 48