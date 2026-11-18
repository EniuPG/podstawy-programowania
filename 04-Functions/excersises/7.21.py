# Returns difference between largest and smallest number

def f(number1, number2, number3):  # definicja funkcji

    largest = max(number1, number2, number3)  # największa liczba

    smallest = min(number1, number2, number3)  # najmniejsza liczba

    return largest - smallest  # zwrócenie różnicy

print(f(7, 4, 9))  # 5

print(f(2, 12, 8))  # 10