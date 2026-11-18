from text_utils import count_letter  # import funkcji

def main():  # funkcja główna

    text = "You never get a second chance to make a first impression"  # tekst

    result = count_letter(text, "a")  # zliczenie a

    print("The number of letter 'a':", result)  # wynik

if __name__ == "__main__":

    main()