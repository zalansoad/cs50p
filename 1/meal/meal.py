def main():
    time = input("Time: ")
    mealtime = convert(time)

    if 7.0 <= mealtime <= 8.0:
        print("breakfast time")
    elif 12.0 <= mealtime <= 13.0:
        print("lunch time")
    elif 18.0 <= mealtime <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    floattime = float(minutes)/60
    return float(hours) + floattime

if __name__ == "__main__":
    main()
