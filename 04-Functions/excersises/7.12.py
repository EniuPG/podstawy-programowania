# Returns stars separated by slashes

def f(n):  # definicja funkcji

    return "/*".join(["*"] * n)  # tworzenie napisu

print(f(4))  # */*/*/*

print(f(1))  # *