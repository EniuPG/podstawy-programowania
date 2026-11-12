# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%

total_tasks = 20  # całkowita liczba zadań
tasks_ok = int(input("Number of correct tasks: "))  # liczba poprawnych odpowiedzi
test_passed = False  # początkowo test nie jest zaliczony

if tasks_ok >= total_tasks / 2:  # sprawdzenie czy wynik to minimum 50%
    test_passed = True  # oznaczenie zaliczenia testu

if test_passed:  # jeśli test zaliczony
    print("Congratulations! You passed the test.")  # komunikat o zaliczeniu
else:  # jeśli test niezaliczony
    print("Unfortunately, you failed the test.")  # komunikat o niezaliczeniu
    
    #20, 11, 10, 9, 0