# Hides card number

def hide(card_number):  # funkcja ukrywająca numer

    return card_number[:2] + "*" * 10 + card_number[-4:]  # wynik