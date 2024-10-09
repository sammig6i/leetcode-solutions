#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res
        
            


# @lc code=end
