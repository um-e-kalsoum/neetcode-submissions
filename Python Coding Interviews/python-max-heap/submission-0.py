import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    new=[]
    max_heap = []

    for i in nums:
        heapq.heappush(max_heap, -i)

    while max_heap:
        first = -heapq.heappop(max_heap)
        new.append(first)
    return new





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
