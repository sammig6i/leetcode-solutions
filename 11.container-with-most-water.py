#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxWater = 0

        while L < R:
            if height[L] <= height[R]:
                area = height[L] * (R - L)
                maxWater = max(area, maxWater)
                L += 1
            else:
                area = height[R] * (R - L)
                maxWater = max(area, maxWater)
                R -= 1
        return maxWater


# @lc code=end
