def get_count(input_str):
    num_vowels = 0
    # your code here
    vocales = ["a", "e", "i", "o", "u"]
    lista = list(input_str)
    vowels = []
    for i in lista:
        for j in vocales:
            if i == j:
                num_vowels += 1

    print(num_vowels)
    return num_vowels

string = input("Please, enter your string: ")
get_count(string)