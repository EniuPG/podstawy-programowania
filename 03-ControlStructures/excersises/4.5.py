# Encrypts text using Caesar Code

plain_text = "The early bird catches the worm"  # tekst do zaszyfrowania
encrypted_text = ""  # pusty napis na zaszyfrowany tekst

for char in plain_text:  # przejście przez każdy znak tekstu

    code = ord(char)  # pobranie kodu ASCII znaku

    code = code + 1  # zwiększenie kodu o 1

    encrypted_char = chr(code)  # zamiana kodu na znak

    encrypted_text += encrypted_char  # dodanie znaku do wyniku

print(f"Plain text: {plain_text}")  # wyświetlenie tekstu źródłowego
print(f"Encrypted text: {encrypted_text}")  # wyświetlenie szyfru