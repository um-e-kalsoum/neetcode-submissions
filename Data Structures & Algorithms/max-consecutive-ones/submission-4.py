class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        curSum = 0
        maxSum = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curSum += 1
                maxSum = max(curSum, maxSum)
            else:
                curSum = 0
        return maxSum
        