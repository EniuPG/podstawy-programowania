# Checks palindrome

def f(palindrome):  # definicja funkcji

    return palindrome == palindrome[::-1]  # porównanie z odwróceniem

print(f("radar"))  # True

print(f("12-11-21"))  # True

print(f("book"))  # False