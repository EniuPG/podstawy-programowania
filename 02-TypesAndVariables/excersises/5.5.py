# Program obliczający cenę po rabacie

price = float(input("Enter price: "))       # Wczytanie ceny produktu

discount = float(input("Enter discount %: "))  # Wczytanie procentu rabatu

reduction = price * discount / 100          # Obliczenie wartości rabatu

discounted_price = price - reduction        # Cena po obniżce

print(f"Price: {price:.2f}")                # Cena początkowa

print(f"Discount: {discount:.0f}%")         # Wartość rabatu

print(f"Price with discount: {discounted_price:.2f}")  # Cena po rabacie

print(f"Reduction: {reduction:.2f}")        # Wielkość obniżki