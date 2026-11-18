# ICAO spelling

def icao(letter):  # definicja funkcji

    codes = {  # słownik ICAO

        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }

    return codes[letter]  # zwrot kodu

name = input("Enter name: ").upper()  # pobranie imienia

for letter in name:  # przejście po literach

    print(icao(letter))  # wyświetlenie słowa ICAO