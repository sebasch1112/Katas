def disemvowel(string_):
    vowels = "aeiouAEIOU"
    for x in range(len(vowels)):
        string_ = string_.replace(vowels[x], "")

    print(string_)
    return string_

phrase = input("Please enter a phrase: ")
disemvowel(phrase)