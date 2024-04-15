def main():
    tweet = input("Input: ")
    print(shorten(tweet))


def shorten(word):
    twt = ""
    for letter in word:
        if letter.casefold() not in "aeiou":
            twt += letter
    return twt


if __name__ == "__main__":
    main()
