# Determines point position

x = int(input("Enter x: "))  # współrzędna x
y = int(input("Enter y: "))  # współrzędna y

if x > 0 and y > 0:  # I ćwiartka

    print(f"Point P({x},{y}) is in the first quadrant")

elif x < 0 and y > 0:  # II ćwiartka

    print(f"Point P({x},{y}) is in the second quadrant")

elif x < 0 and y < 0:  # III ćwiartka

    print(f"Point P({x},{y}) is in the third quadrant")

elif x > 0 and y < 0:  # IV ćwiartka

    print(f"Point P({x},{y}) is in the fourth quadrant")

elif x == 0 and y == 0:  # punkt początkowy

    print("Point is at (0,0)")

elif x == 0:  # oś Y

    print("Point lies on Y axis")

else:  # oś X

    print("Point lies on X axis")