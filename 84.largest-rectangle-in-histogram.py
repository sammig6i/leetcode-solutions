#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                lastIndex, lastHeight = stack.pop()
                area = lastHeight * (i - lastIndex)
                maxArea = max(area, maxArea)
                startIndex = lastIndex
            stack.append((startIndex, h))

        while stack:
            index, height = stack.pop()
            area = height * (len(heights) - index)
            maxArea = max(area, maxArea)
        
        return maxArea


# @lc code=end
