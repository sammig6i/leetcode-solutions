#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empties = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((empties - 1) / 2)
                empties = 0
            else:
                empties += 1
        
        n -= (empties) // 2
        return n <= 0

# @lc code=end
