# Program odczytujący kod SWIFT

swift = input("Enter SWIFT code: ")   # Wczytanie kodu SWIFT

bank_code = swift[0:4]                # Kod banku

country_code = swift[4:6]             # Kod kraju

print(f"Bank Code: {bank_code}")      # Wyświetlenie kodu banku

print(f"Country Code: {country_code}") # Wyświetlenie kodu kraju