class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxR = -1
        new = []

        for i in range(len(arr)-1, -1, -1):
            new.append(maxR)
            maxR = max(maxR, arr[i])
        return new[::-1]