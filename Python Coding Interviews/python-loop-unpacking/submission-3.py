from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    bestn = ""
    highs = 0

    for n,v in scores:
        if v>highs:
            highs = v
            bestn = n
    return bestn


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
