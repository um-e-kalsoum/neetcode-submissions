class Solution:
    def maxArea(self, heights: List[int]) -> int:

        currVol = 0
        maxVol = 0

        L = 0
        R = len(heights) - 1

        while L < R:
            width = R - L
            height = min(heights[R], heights[L])
            currVol = width * height
            maxVol = max(maxVol, currVol)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return maxVol

        