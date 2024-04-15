while True:
    try:
        x, y = input("Fraction: ").split("/")
        if int(x) > int(y):
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        pass

percentage = (int(x) / int(y)) * 100

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f'{percentage:.0f}%')




