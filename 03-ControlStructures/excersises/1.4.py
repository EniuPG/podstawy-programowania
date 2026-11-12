# Credit card payment

account_balance = 500  # stan konta klienta
total_payment = float(input("Enter payment amount: "))  # pobranie kwoty zakupu

if total_payment <= account_balance:  # sprawdzenie czy są wystarczające środki
    print("Payment completed")  # informacja o udanej płatności
else:  # gdy środków jest za mało
    print("No funds")  # informacja o braku środków
    
    
    #140, 499, 500, 501, 720