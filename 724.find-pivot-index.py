#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - nums[i] - left_sum
            if right_sum == left_sum:
                return i
            else:
                left_sum += nums[i]
        return -1


# @lc code=end
