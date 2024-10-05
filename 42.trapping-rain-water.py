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
        L = 0
        R = len(height) - 1
        maxL, maxR = 0, 0

        for i in range(len(height)):
            while L < R:
                maxL = max(height[L], maxL)
                maxR = max(height[R], maxR)

                if maxL <= maxR:
                    waterCount += max(0, maxL - height[L])
                    L += 1
                else:
                    waterCount += max(0, maxR - height[R])
                    R -= 1

        return waterCount


# @lc code=end
