class Solution:
    def isValid(self, s: str) -> bool:

        sets = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        ans = []
        
        for b in s:
            if b == '(' or b == '[' or b == '{':
                ans.append(b)
            elif ans and ans[-1] == sets[b]:
                ans.pop()

            else:
                return False
        return not ans