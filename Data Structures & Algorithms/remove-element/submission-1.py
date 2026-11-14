class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1 # only inc when the value != the elem
                        # this will give us the total amount of vals in the array that != val
        return k 

        