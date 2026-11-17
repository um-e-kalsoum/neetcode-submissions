class Solution:
    def isPalindrome(self, s: str) -> bool:

        lowerCase = s.lower()
        new = ''

        for letter in lowerCase:
            if letter.isalnum():
                new += letter
        
        L = 0
        R = len(new)-1

        while L < R:
            if new[L] == new[R]:
                L += 1
                R -= 1
            else:
                return False
        return True
        