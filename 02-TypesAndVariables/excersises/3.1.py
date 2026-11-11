company = "ABC Data"                  # Nazwa firmy (tekst)
phone = "555-123-009"                 # Numer telefonu (tekst)
employees = 25                        # Liczba pracowników (liczba całkowita)
remote_work = True                    # Praca zdalna dozwolona (wartość logiczna)
big_company = employees > 100         # Sprawdzenie czy firma ma ponad 100 pracowników
income = 4500000                      # Dochód firmy (liczba całkowita)
income_per_person = income / employees # Dochód na jednego pracownika

print(type(company))                  # Wyświetla typ str
print(type(phone))                    # Wyświetla typ str
print(type(employees))                # Wyświetla typ int
print(type(remote_work))              # Wyświetla typ bool
print(type(big_company))              # Wyświetla typ bool
print(type(income))                   # Wyświetla typ int
print(type(income_per_person))        # Wyświetla typ float