# Program obliczający podatek VAT 23%

amount = float(input("Enter amount: "))   # Wczytanie kwoty

vat = amount * 0.23                       # Obliczenie VAT

print(f"Amount   : {amount:.2f}")         # Kwota z dwoma miejscami po przecinku

print(f"VAT 23%  : {vat:.2f}")           # VAT z dwoma miejscami po przecinku