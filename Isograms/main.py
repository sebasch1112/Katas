def is_isogram(string):
    # your code here

    isogram = True
    lista = list(string)

    for i in lista:
        num = lista.count(i) + lista.count(i.upper()) + lista.count(i.lower())
        if num >= 3:
            isogram = False

        elif num == 0:
            isogram = True

    print(isogram)
    return isogram

string = input("Please, enter a stirng: ")
is_isogram(string)

