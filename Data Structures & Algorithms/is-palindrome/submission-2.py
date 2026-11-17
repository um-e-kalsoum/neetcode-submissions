class Solution:
    def isPalindrome(self, s: str) -> bool:

        letters = []

        for c in s:
            if c.isalnum():
                letters.append(c.lower())

        L = 0
        R = len(letters) - 1

        while L < R:
            if letters[L] == letters[R]:
                L += 1
                R -= 1
            else:
                return False
        return True




        