class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        new = []

        for i in range(len(arr)):
            maxR = -1
            for j in range(i+1, len(arr)):
                maxR = max(maxR, arr[j])
            new.append(maxR)
        return new

        