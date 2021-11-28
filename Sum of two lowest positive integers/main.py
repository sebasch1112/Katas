# Here we start writing the solution
#for this kata we just need to define our function
def sum_two_smallest_numbers(numbers):
    # your code here
    numbers.sort()

    suma = numbers[0] + numbers[1]
    print(suma)
    return suma
list = []
a = int(input("Please, type the lenght of your array: "))
for i in range(a):
    b = int(input("Type a number: "))
    list.append(b)
sum_two_smallest_numbers(list)