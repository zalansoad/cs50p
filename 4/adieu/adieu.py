import inflect
p = inflect.engine()

name_list = []
greet = "Adieu, adieu, to"
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        mylist = p.join(name_list)
        print(greet, mylist)
        break
