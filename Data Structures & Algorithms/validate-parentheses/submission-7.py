class Solution:
    def isValid(self, s: str) -> bool:

        sets = {')':'(', ']':'[', '}':'{'}
        new = []

        for b in s:
            if b == '(' or b == '[' or b == '{':
                new.append(b)
                continue
            if new and new[-1] == sets[b]:
                new.pop()
            else:
                return False
        return not new

        