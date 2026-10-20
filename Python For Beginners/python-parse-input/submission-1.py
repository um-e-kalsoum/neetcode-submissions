from typing import List

def read_integers() -> List[int]:
    userin = input()    #read line
    ints = [int(x) for x in userin.split(",")] #typecast to int, declare each value an x(int) sep by comma
    return ints

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
