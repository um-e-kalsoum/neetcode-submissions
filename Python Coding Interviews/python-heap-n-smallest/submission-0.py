import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    x = heapq.nsmallest(1,arr)
    return x[0]

def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    new=heapq.nsmallest(4, arr)
    return new


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    new=heapq.nsmallest(2,arr)
    new.sort(reverse=True)
    return new


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

