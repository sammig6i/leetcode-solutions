#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], right_max)
            arr[i] = right_max
            right_max = new_max
        return arr


# @lc code=end
