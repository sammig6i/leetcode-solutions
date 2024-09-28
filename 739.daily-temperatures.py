#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                lastIndex, lastTemp = stack.pop()
                res[lastIndex] = index - lastIndex
            stack.append((index, temp))
        return res


# @lc code=end
