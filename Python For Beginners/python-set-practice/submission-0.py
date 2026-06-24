from typing import List

def contains_duplicate(words: List[str]) -> bool:
    s = set(words)
    l_set = len(s)
    l_list = len(words)
    if l_set != l_list:
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
