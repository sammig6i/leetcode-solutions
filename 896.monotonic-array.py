#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            if not (nums[i] <= nums[i + 1]):
                increasing = False
            elif not (nums[i] >= nums[i + 1]):
                decreasing = False

        return increasing or decreasing


# @lc code=end
