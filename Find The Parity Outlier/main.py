def find_outlier(integers):
    result = 0

    even = []
    odd = []

    for i in range(0, 3):
        num = integers[i] % 2
        if num == 0:
            even.append(integers[i])
        else:
            odd.append(integers[i])

    if len(even) == 3:
        for j in integers:
            if j % 2 != 0:
                result = j


    elif len(even) == 1:
        result = even[0]

    elif len(even) == 0:
        for k in integers:
            if k % 2 == 0:
                result = k

    else:
        result = odd[0]

    print(result)
    return result
list = []
a = int(input("Please, type the lenght of your array: "))
for i in range(a):
    b = int(input("Please enter a number: "))
    list.append(b)

find_outlier(list)

