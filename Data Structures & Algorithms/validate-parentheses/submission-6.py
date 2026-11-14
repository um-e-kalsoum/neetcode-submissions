class Solution:
    def isValid(self, s: str) -> bool:

        tmp = []
        sets = {')':'(', '}' : '{', ']' : '['}
        for b in s:
            if b not in sets:
                tmp.append(b)
                continue
            if tmp and tmp[-1] == sets[b]:
                tmp.pop()
            else:
                return False
        return not tmp