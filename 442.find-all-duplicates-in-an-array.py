#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] = -nums[n - 1]
        return res


# @lc code=end
