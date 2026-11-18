# Password validator

def f(password):  # definicja funkcji

    if len(password) < 6:  # sprawdzenie długości

        return False  # hasło za krótkie

    if len(password) != len(set(password)):  # sprawdzenie powtórzeń

        return False  # powtarzające się znaki

    return True  # poprawne hasło

print(f("ax15"))  # False

print(f("book123"))  # False

print(f("A2water3"))  # True

print(f("qwerty"))  # True

print(f(""))  # False