# Calculates dog's age in dog years

human_years = int(input("Enter the dog's age in human years: "))  # pobranie wieku psa

if human_years <= 2:  # dla pierwszych dwóch lat

    dog_years = human_years * 10.5  # 10.5 roku psa za każdy rok

else:  # dla wieku powyżej dwóch lat

    dog_years = 21 + (human_years - 2) * 4  # kolejne lata po 4 lata psa

print(f"The dog's age in dog's years is {dog_years} years.")  # wyświetlenie wyniku