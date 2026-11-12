 #A program for checking clothing sizes

size = input("Enter size symbol: ")  # pobranie symbolu rozmiaru

if size == "S":  # sprawdzenie czy rozmiar to S
    print("S: Small size")  # wyświetlenie opisu rozmiaru S
elif size == "M":  # sprawdzenie czy rozmiar to M
    print("M: Medium size")  # wyświetlenie opisu rozmiaru M
elif size == "L":  # sprawdzenie czy rozmiar to L
    print("L: Large size")  # wyświetlenie opisu rozmiaru L
elif size == "XL":  # sprawdzenie czy rozmiar to XL
    print("XL: Extra large size")  # wyświetlenie opisu rozmiaru XL
else:  # jeśli podano niepoprawny symbol
    print("Incorrect symbol")  # komunikat o błędnym symbolu