#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        waterCount = 0
        L, R = 0, len(height) - 1
        maxL = 0
        maxR = 0

        while L < R:
            maxL = max(maxL, height[L])
            maxR = max(maxR, height[R])

            if maxL <= maxR:
                waterCount += maxL - height[L]
                L += 1
            else:
                waterCount += maxR - height[R]
                R -= 1
        return waterCount


# @lc code=end
