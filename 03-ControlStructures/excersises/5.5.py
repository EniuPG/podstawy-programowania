# Sums numbers entered by user and calculates average

total_sum = 0  # suma liczb
count = 0  # licznik wprowadzonych liczb

while True:  # pętla nieskończona

    number = int(input("Enter a number (0 to stop): "))  # pobranie liczby

    if number == 0:  # sprawdzenie warunku zakończenia
        break  # wyjście z pętli

    total_sum += number  # dodanie liczby do sumy
    count += 1  # zwiększenie licznika

if count > 0:  # sprawdzenie czy podano liczby
    average = total_sum / count  # obliczenie średniej
else:  # jeśli nie podano żadnej liczby
    average = 0  # średnia równa zero

print(f"The total sum of the numbers is: {total_sum}")  # wyświetlenie sumy
print(f"The arithmetic mean is: {average}")  # wyświetlenie średniej