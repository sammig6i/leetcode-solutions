#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        SMap = {}
        TMap = {}

        for c1, c2 in zip(s, t):
            SMap[c1] = 1 + SMap.get(c1, 0)
            TMap[c2] = 1 + TMap.get(c2, 0)
        return SMap == TMap
            
        
# @lc code=end

