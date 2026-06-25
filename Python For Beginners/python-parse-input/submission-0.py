from typing import List

def read_integers() -> List[int]:
    str_input = input()
    list_input = str_input.split(",")
    for i in range(len(list_input)):
        list_input[i] = int(list_input[i])
    return list_input

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
