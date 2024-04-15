import re
import sys


def main():
    print(parse(input("HTML: ")))



def parse(s):
    matches = re.search(r"^\<iframe.*?src\=\"https?\:\/\/(www\.)?youtube\.com\/embed\/(.+?)\".+", s)
    if matches:
        a ="https://youtu.be/"
        b = matches.group(2)
        return(a + b)
    else:
        return None



...


if __name__ == "__main__":
    main()
