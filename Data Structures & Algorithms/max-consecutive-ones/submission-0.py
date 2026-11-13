class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        maxseq = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > maxseq:
                    maxseq = count
            elif nums[i] == 0:
                count = 0
        return maxseq
        