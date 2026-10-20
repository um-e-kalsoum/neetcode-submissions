def add_two_numbers() -> int:
    userin = input()
    ints = [int(x) for x in userin.split(",")]
    add= sum(ints)
    return add



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
