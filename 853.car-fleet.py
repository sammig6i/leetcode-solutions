#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]

        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)


# @lc code=end
