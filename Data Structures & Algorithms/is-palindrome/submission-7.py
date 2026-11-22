class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = []

        for l in s:
            if l.isalnum():
                new += l.lower()
        
        L = 0
        R = len(new)-1

        while L < R:
            if new[L] == new[R]:
                L+=1
                R-=1
            else:
                return False
        return True
            

        