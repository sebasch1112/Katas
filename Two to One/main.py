def longest(a1, a2):
    # your code
    lista1 = list(a1)
    lista2 = list(a2)

    string = []

    for i in lista1:
        if string.count(i) == 0:
            if lista1.count(i) >= 1:
                if lista2.count(i) >= 0:
                    string.append(i)
    for j in lista2:
        if lista2.count(j) >= 1:
            if string.count(j) == 0:
                string.append(j)
    string2 = "".join(sorted(string))
    print(string2)
    return string2

first_string = input("Please, enter an string: ")
second_string = input("Please, enter an string: ")

longest(first_string, second_string)
