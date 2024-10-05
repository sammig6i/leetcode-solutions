#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                threeSum = nums[i] + nums[L] + nums[R]
                if threeSum < 0:
                    L += 1
                elif threeSum > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return res


# @lc code=end
