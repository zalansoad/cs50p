expression = input("Calculator: ")
x, y, z = expression.split(" ")

if y == "+":
        result = float(x) + float(z)
        print(f"{result:.1f}")

elif y == "-":
        result = float(x) - float(z)
        print(f"{result:.1f}")

elif y == "*":
        result = float(x) * float(z)
        print(f"{result:.1f}")

elif  y == "/":
        result = float(x) / float(z)
        print(f"{result:.1f}")






