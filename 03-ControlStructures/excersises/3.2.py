# Checking login and password

login = "JJ2006"  # poprawny login
password = "2137"  # poprawne hasło

entered_login = input("Login: ")  # pobranie loginu od użytkownika
entered_password = input("Password: ")  # pobranie hasła od użytkownika

if login == entered_login and password == entered_password:  # sprawdzenie loginu i hasła
    print("You are logged in")  # komunikat poprawnego logowania
else:  # jeśli login lub hasło są błędne
    print("Incorrect login or password!!")  # komunikat błędu