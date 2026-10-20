from typing import List

def read_integers() -> List[int]:
    userin = input()
    ints = [int(x) for x in userin.split(",")]
    return ints

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
