#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(original) != (m * n):
            return res
        
        row = []
        for i in original:
            row.append(i)
            if len(row) == n:
                res.append(row)
                row = []
        return res




# @lc code=end
