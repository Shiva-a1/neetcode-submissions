def add_two_numbers() -> int:
    list_input = input().split(',')
    sum = 0
    for i in list_input:
        sum+=int(i)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
