# Calculator function

def f(number1, number2, operator):  # definicja funkcji

    if operator == "+":  # dodawanie
        return number1 + number2

    elif operator == "-":  # odejmowanie
        return number1 - number2

    elif operator == "*":  # mnożenie
        return number1 * number2

    elif operator == "%":  # modulo
        return number1 % number2

    elif operator == "**":  # potęgowanie
        return number1 ** number2

print(f(2, 3, "+"))  # 5

print(f(2, 3, "%"))  # 2

print(f(2, 3, "**"))  # 8

print(f(2, 3, "*"))  # 6

print(f(2, 3, "-"))  # -1