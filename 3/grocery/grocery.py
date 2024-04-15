grocery = []
dictionary_grocery = {}
while True:
    try:
        item = input()
        grocery.append(item)

    except EOFError:
        sorted_grocery = sorted(grocery)

        for i in sorted_grocery:
            if i not in dictionary_grocery.keys():
                dictionary_grocery[i] = 1
            else:
                dictionary_grocery[i] = dictionary_grocery[i] + 1

        print(dictionary_grocery.items())
        for key, value in dictionary_grocery.items():
            print(value, key.upper())
        break
