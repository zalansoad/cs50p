def main():
    sentence = input("Your sentence: ")
    convert(sentence)

def convert(x):
    x = x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    print(x)

main()


