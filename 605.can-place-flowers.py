#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1
        n -= (empty) // 2
        return n <= 0


# @lc code=end
