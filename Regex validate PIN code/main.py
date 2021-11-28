def validate_pin(pin):
    # return true or false
    Bool = True
    numeros = "0123456789"
    num_list = list(numeros)

    pin_list = list(pin)

    digits = len(pin_list)

    if digits == 4 or digits == 6:
        for i in pin_list:
            if num_list.count(i) == 0:
                Bool = False
    else:
        Bool = False

    print(Bool)
    return Bool

PIN = input("Please, enter your PIN: ")
validate_pin(PIN)