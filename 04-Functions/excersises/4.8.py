# Returns time as string

def time_string(hours, minutes, time_format):  # definicja funkcji

    if time_format == "24":  # format 24h

        return f"{hours:02d}:{minutes:02d}"

    if hours == 0:  # północ

        return f"12:{minutes:02d}am"

    elif hours < 12:  # przed południem

        return f"{hours}:{minutes:02d}am"

    elif hours == 12:  # południe

        return f"12:{minutes:02d}pm"

    else:  # po południu

        return f"{hours-12}:{minutes:02d}pm"

print(time_string(15, 38, "24"))
print(time_string(8, 3, "24"))
print(time_string(0, 5, "24"))
print(time_string(11, 15, "12"))
print(time_string(0, 7, "12"))
print(time_string(7, 30, "12"))
print(time_string(12, 46, "12"))
print(time_string(13, 10, "12"))
print(time_string(19, 2, "12"))