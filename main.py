
print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print()

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

Choice = int(input("Your choice: "))

if Choice == 1:
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")

    SubChoice = int(input("Your choice: "))

    if SubChoice == 1:
        Meters = float(input("Insert meters: "))

        Kilometers = Meters / 1000
        Kilometers = round(Kilometers, 1)

        print(f"{Meters} m is {Kilometers} km")

    elif SubChoice == 2:
        Kilometers = float(input("Insert kilometers: "))

        Meters = Kilometers * 1000
        Meters = round(Meters, 1)

        print(f"{Kilometers} km is {Meters} m")

    elif SubChoice == 0:
        print("Exiting...")

    else:
        print("Unknown option.")

elif Choice == 2:
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")

    SubChoice = int(input("Your choice: "))

    if SubChoice == 1:
        Grams = float(input("Insert grams: "))

        Pounds = Grams / 453.59237
        Pounds = round(Pounds, 1)

        print(f"{Grams} g is {Pounds} lb")

    elif SubChoice == 2:
        Pounds = float(input("Insert pounds: "))

        Grams = Pounds * 453.59237
        Grams = round(Grams, 1)

        print(f"{Pounds} lb is {Grams} g")

    elif SubChoice == 0:
        print("Exiting...")

    else:
        print("Unknown option.")

elif Choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print()
print("Program ending.")