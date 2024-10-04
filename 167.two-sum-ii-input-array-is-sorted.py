#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            twoSum = numbers[i] + numbers[j]

            if twoSum > target:
                j -= 1
            elif twoSum < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return -1
        
# @lc code=end

