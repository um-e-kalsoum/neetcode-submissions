class Solution:
    def trap(self, height: List[int]) -> int:

        totalWater = 0
        
        L = 0
        R = len(height)-1

        left_max = height[L]
        right_max = height[R]

        while L < R:
            if left_max <= right_max:
                L += 1
                left_max = max(left_max, height[L])
                totalWater += left_max - height[L]
            else:
                R -= 1
                right_max = max(right_max, height[R])
                totalWater += right_max - height[R]
        return totalWater





        