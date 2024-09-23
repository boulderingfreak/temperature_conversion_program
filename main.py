print("Hi in my temperature converter")

choice = int(input("Type 1 to convert Celsiuses into Farenheits. \nType 2 to convert Farenheits into Celsiuses. \nYour choice: "))

if choice == 1:
    c = float(input("C: "))
    result = (c * 9/5) + 32
    print(f"{c} Celsiuses is {round(result, 1)} Farenheits.")
elif choice == 2:
    f = float(input("F: "))
    result = (f - 32) * 5/9
    print(f"{f} Farenheits is {round(result, 1)} Celsiuses.")
else:
    print("Type 1 or 2 you dumb")