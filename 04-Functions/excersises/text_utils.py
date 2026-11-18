# Counts letters in text

def count_letter(text, letter):  # funkcja licząca znaki

    count = 0  # licznik

    for char in text:  # przejście po tekście

        if char.lower() == letter.lower():  # porównanie liter

            count += 1  # zwiększenie licznika

    return count  # zwrot wyniku