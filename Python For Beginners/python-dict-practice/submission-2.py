from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    num = {}

    for i in word:
        if i in num:
            num[i] += 1
        else:
            num[i] = 1

    return num




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
