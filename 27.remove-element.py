#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1
            else:
                i += 1
        return n


# @lc code=end
