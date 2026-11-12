# Influencer checker

facebook = True  # konto Facebook
twitter = False  # konto Twitter
instagram = False  # konto Instagram

accounts = 0  # licznik kont

if facebook:  # jeśli ma Facebook
    accounts += 1  # zwiększ licznik

if twitter:  # jeśli ma Twitter
    accounts += 1  # zwiększ licznik

if instagram:  # jeśli ma Instagram
    accounts += 1  # zwiększ licznik

if accounts >= 2:  # minimum dwa konta

    print("You are a good influencer!")  # komunikat
else:  # mniej niż dwa konta
    print("You need to improve your social media presence!")  # komunikat