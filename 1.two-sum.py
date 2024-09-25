#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the complement of each number
        complement_dict = {}
        
        # Iterate through the list with index
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in complement_dict:
                # If found, return the indices of the two numbers
                return [complement_dict[complement], i]
            
            # If not found, add the current number and its index to the dictionary
            complement_dict[num] = i
        
        # If no solution is found, return an empty list or raise an exception
        return []  # or raise ValueError("No two sum solution")
        

        
        
# @lc code=end