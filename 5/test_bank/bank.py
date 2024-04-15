def main():
    greet = input("Greet: ")
    print(f"${value(greet)}")


def value(greeting: str):
    greeting = greeting.casefold().strip()
    if greeting.startswith("hello"):
        return 0

    elif greeting.startswith("h"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
