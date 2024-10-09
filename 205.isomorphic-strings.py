#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        STmap, TSmap = {}, {}
        for s, t in zip(s, t):
            if s in STmap and STmap[s] != t or t in TSmap and TSmap[t] != s:
                return False
            STmap[s] = t
            TSmap[t] = s
        return True


# @lc code=end
