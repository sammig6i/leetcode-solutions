#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for _ in range(numRows - 1):
            prev_row = [0] + res[-1] + [0]
            j = 0
            k = j + 1
            new_row = []
            while k < len(prev_row):
                new_row.append(prev_row[j] + prev_row[k])
                j += 1
                k += 1
            res.append(new_row)
        return res       


# @lc code=end
