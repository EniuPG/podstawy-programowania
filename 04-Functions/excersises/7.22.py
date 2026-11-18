# Returns acronym

def f(name):  # definicja funkcji

    words = name.split()  # podział tekstu na słowa

    acronym = ""  # pusty skrót

    for word in words:  # przejście po słowach

        acronym += word[0]  # dodanie pierwszej litery

    return acronym  # zwrócenie skrótu

print(f("Internet of Things"))  # IoT

print(f("For Your Information"))  # FYI

print(f("Python"))  # P