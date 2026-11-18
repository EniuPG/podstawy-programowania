# Checks if at least one number is negative

def f(n1, n2, n3): # definicja funkcji
    return n1 < 0 or n2 < 0 or n3 < 0 # zwrócenie wyniku

print(f(11, 6, -4)) # True

print(f(5, 4, 14)) # False