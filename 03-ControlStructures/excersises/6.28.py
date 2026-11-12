# Fibonacci sequence

a = 0  # pierwszy wyraz
b = 1  # drugi wyraz

for i in range(20):  # 20 wyrazów

    print(a, end=" ")  # wyświetlenie wyrazu

    next_number = a + b  # następny wyraz

    a = b  # przesunięcie

    b = next_number  # przesunięci