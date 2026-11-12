# Calculates purchase amount

quantity = int(input("Number of products purchased: "))  # liczba produktów
price = float(input("Product price: "))  # cena jednego produktu

if quantity > 2:  # jeśli kupiono więcej niż 2 produkty

    full_price = 2 * price  # pierwsze dwa produkty bez rabatu

    discounted_price = (quantity - 2) * price * 0.75  # pozostałe z rabatem 25%

    total = full_price + discounted_price  # suma do zapłaty

else:  # jeśli 2 lub mniej produktów

    total = quantity * price  # zwykła cena

print(f"Amount to pay: {total:.2f}")  # wyświetlenie kwoty