from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "-font":
        sys.exit("Invalid usage")
    else:
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            text = input("Input: ")
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")




