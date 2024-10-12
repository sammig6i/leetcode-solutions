#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        return False
        
# @lc code=end

