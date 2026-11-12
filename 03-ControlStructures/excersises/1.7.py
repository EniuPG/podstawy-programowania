# Program that calculates the employee's salary
# taking into account the possibility of receiving a bonus

basic_salary = 5000  # podstawowa pensja pracownika
total_salary = 0  # zmienna na całkowite wynagrodzenie
bonus = 0.3  # premia 30%
is_bonus = input("Does the employee receive a bonus? (Y/N): ") == "Y"  # sprawdzenie czy jest premia

if is_bonus:  # jeśli pracownik otrzymuje premię
    total_salary = basic_salary + (basic_salary * bonus)  # obliczenie pensji z premią
else:  # jeśli nie ma premii
    total_salary = basic_salary  # pensja równa podstawie

print(f"Basic salary: {basic_salary}")  # wyświetlenie pensji podstawowej
print(f"Bonus included? {is_bonus}")  # informacja czy dodano premię
print(f"Total salary: {total_salary}")  # wyświetlenie całkowitej pensji