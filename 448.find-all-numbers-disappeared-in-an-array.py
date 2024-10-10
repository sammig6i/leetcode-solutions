#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res



# @lc code=end
