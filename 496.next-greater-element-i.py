#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = nums2[i]
            if nums2[i] in nums1Idx:
                stack.append(nums2[i])
        return res


# @lc code=end
