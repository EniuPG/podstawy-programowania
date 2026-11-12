# Converts 24-hour format to 12-hour format

time24 = input("Enter time (24-hour format): ")  # pobranie czasu

hours, minutes = time24.split(":")  # rozdzielenie godzin i minut

hours = int(hours)  # zamiana na liczbę

if hours == 0:  # północ

    hours12 = 12  # format 12h

    suffix = "am"  # oznaczenie

elif hours < 12:  # przed południem

    hours12 = hours  # bez zmian

    suffix = "am"  # oznaczenie

elif hours == 12:  # południe

    hours12 = 12  # bez zmian

    suffix = "pm"  # oznaczenie

else:  # po południu

    hours12 = hours - 12  # konwersja

    suffix = "pm"  # oznaczenie

print(f"Time in 12-hour format: {hours12}:{minutes}{suffix}")  # wynik