# Checks if entered name is a Polish female name

name = input("Enter name: ")  # pobranie imienia

if name.endswith("a"):  # większość polskich imion żeńskich kończy się na a

    print(f"{name} -- Polish female name")  # wyświetlenie komunikatu

else:  # jeśli nie kończy się na a

    print(f"{name} -- not a typical Polish female name")  # komunikat