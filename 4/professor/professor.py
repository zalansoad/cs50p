import random

list = []

def main():
    score = 10

    level = get_level()
    for i in range(10):
        counter = 0
        a = generate_integer(level)
        b = generate_integer(level)
        addition = a + b
        inputstring = " ".join([str(a), "+", str(b), "= "])

        while True:
            try:
                answer = int(input(inputstring))
            except ValueError:
                print("EEE")
                counter += 1
                if counter == 3:
                    print(inputstring + str(addition))
                    break
            else:
                if answer == addition:
                    break
                else:
                    print("EEE")
                    counter += 1
                    if counter == 3:
                        print(inputstring + str(addition))
                        break


        if counter > 0:
            score -= 1
    print("Score:", score)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n

        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
