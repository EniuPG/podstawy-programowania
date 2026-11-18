# Returns month name

def month(n):  # funkcja zwracająca nazwę miesiąca

    months = [  # lista miesięcy
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if 1 <= n <= 12:  # sprawdzenie zakresu
        return months[n - 1]  # zwrócenie nazwy miesiąca

    return "Incorrect month"  # błędny numer