# Keyboard functions

def input_string(message):  # odczyt tekstu

    value = input(message)

    return value

def input_integer(message):  # odczyt liczby całkowitej

    value = int(input(message))

    return value

def input_real(message):  # odczyt liczby rzeczywistej

    value = float(input(message))

    return value

def input_boolean(message):  # odczyt wartości logicznej

    value = input(message).lower() == "y"

    return value



