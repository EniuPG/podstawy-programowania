# House lighting with three bulbs and two switches

light_switch1 = True  # pierwszy przełącznik
light_switch2 = False  # drugi przełącznik

bulbs_on = 0  # liczba świecących żarówek

if light_switch1:  # jeśli pierwszy przełącznik jest włączony
    bulbs_on += 1  # świeci jedna żarówka

if light_switch2:  # jeśli drugi przełącznik jest włączony
    bulbs_on += 2  # świecą dwie żarówki

print(f"Number of bulbs on: {bulbs_on}")  # wyświetlenie liczby żarówek