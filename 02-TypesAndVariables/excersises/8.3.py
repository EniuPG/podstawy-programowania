# Program odczytuje temperaturę w stopniach Celsjusza
# Następnie przelicza ją na Kelwiny
# oraz stopnie Fahrenheita

celsius = float(input("Enter temperature in Celsius: ")) # Wczytanie temperatury

kelvin = celsius + 273.15 # Zamiana na Kelwiny

fahrenheit = celsius * 9 / 5 + 32 # Zamiana na Fahrenheity

print(f"Temperature in Celsius: {celsius} °C") # Temperatura w °C

print(f"Temperature in Kelvin: {kelvin} K") # Temperatura w K

print(f"Temperature in Fahrenheit: {fahrenheit} °F") # Temperatura w °F