# Calculates final grade

def pts_to_grade(points):  # definicja funkcji

    grade = ""  # zmienna na ocenę

    if points >= 18:  # minimum 18 punktów
        grade = "Excellent"

    elif points >= 14:  # minimum 14 punktów
        grade = "Good"

    elif points >= 10:  # minimum 10 punktów
        grade = "Satisfactory"

    else:  # mniej niż 10 punktów
        grade = "Fail"

    return grade  # zwrot oceny

test_result = 15  # wynik testu

final_grade = pts_to_grade(test_result)  # obliczenie oceny
print(f"You scored {test_result} points. Your final grade is {final_grade}")  # wynik