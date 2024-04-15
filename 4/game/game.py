import random
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass
#generate random int
rn = random.randint(1, n)

while True:
    try:
        guess = int((input("Guess: ")))
    except ValueError:
        pass
    else:
        if guess > 0:
            if guess > rn:
                print("Too large!")
            elif guess < rn:
                print("Too small!")
            else:
                print("Just right!")
                break
