tweet = input("Input: ")
twt = ""

for letter in tweet:
    if letter.casefold() not in "aeiou":
        twt += letter
print(twt)
