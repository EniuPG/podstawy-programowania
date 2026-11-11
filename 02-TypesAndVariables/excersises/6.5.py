# Program formatujący numer telefonu

phone = input("Enter phone number: ")  # Pobranie numeru

formatted = phone[0:3] + "-" + phone[3:6] + "-" + phone[6:9]  # Dodanie myślników

print(f"Phone number: {formatted}")    # Wyświetlenie numeru