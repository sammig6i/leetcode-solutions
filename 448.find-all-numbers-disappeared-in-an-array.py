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
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -1 * abs(nums[idx])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res





# @lc code=end
