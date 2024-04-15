import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(.+:*.*.*? [APM]{2}) to (.+:*.*.*? [APM]{2})$", s)
    if matches:
        a, b = matches.groups()
        if ':' in a:
            start = a.replace(':', ' ').split()
            end = b.replace(':', ' ').split()
            if int(start[0]) > 12 or int(end[0]) > 12:
                raise ValueError
            elif int(start[1]) >= 60 or int(end[1]) >= 60:
                raise ValueError
            else:
                if start[2] == "PM":
                    start[0] = int(start[0]) + 12
                    if start[0] == 24:
                        start[0] = start[0] / 2

                if end[2] == "PM":
                    end[0] = int(end[0]) + 12
                    if end[0] == 24:
                        end[0] = end[0] / 2

                if start[2] == "AM":
                    if int(start[0]) == 12:
                        start[0] = 0

                if end[2] == "AM":
                    if int(end[0]) == 12:
                        end[0] = 0

                return(f"{int(start[0]):02}:{int(start[1]):02} to {int(end[0]):02}:{int(end[1]):02}")

        else:
            start = a.split()
            end = b.split()
            if int(start[0]) > 12 or int(end[0]) > 12:
                raise ValueError
            else:
                if start[1] == "PM":
                    start[0] = int(start[0]) + 12
                    if int(start[0]) == 24:
                        start[0] = int(start[0]) / 2
                if end[1] == "PM":
                    end[0] = int(end[0]) + 12
                    if int(end[0]) == 24:
                        end[0] = int(end[0]) / 2

                if start[1] == "AM":
                    if int(start[0]) == 12:
                        start[0] = 0

                if end[1] == "AM":
                    if int(end[0]) == 12:
                        end[0] = 0

                return(f"{int(start[0]):02}:00 to {int(end[0]):02}:00")
    else:
        raise ValueError




if __name__ == "__main__":
    main()
