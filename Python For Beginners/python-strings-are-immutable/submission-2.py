def remove_fourth_character(word: str) -> str:
    s1 = word[:3]
    s2 = word[4:]
     
    new = s1+s2

    return new

# abcdefg
# 0123456

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
