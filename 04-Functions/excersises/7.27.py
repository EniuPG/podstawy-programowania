# Checks product code

def f(product_code):  # definicja funkcji

    first = int(product_code[0])  # pierwsza cyfra

    second = int(product_code[1])  # druga cyfra

    third = int(product_code[2])  # trzecia cyfra

    control = int(product_code[3])  # cyfra kontrolna

    calculated = (first + second + third) % 7  # obliczenie kontroli

    return calculated == control  # sprawdzenie

print(f("1082"))  # True

print(f("2035"))  # True

print(f("1114"))  # False

print(f("7071"))  # False