# Checking product price reduction

current_price = 140.00  # aktualna cena produktu
previous_price = 200.00  # poprzednia cena produktu

discount_percent = (previous_price - current_price) / previous_price * 100  # obliczenie procentowej obniżki

print(f"Current product price: {current_price:.2f}")  # wyświetlenie aktualnej ceny
print(f"Previous product price: {previous_price:.2f}")  # wyświetlenie poprzedniej ceny

if discount_percent >= 10:  # sprawdzenie czy obniżka wynosi minimum 10%
    print("Buy the product!!")  # rekomendacja zakupu
    print(f"Product price reduced by {discount_percent:.0f}%")  # wyświetlenie obniżki