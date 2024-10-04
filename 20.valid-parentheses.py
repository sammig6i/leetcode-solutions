#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in closedToOpen:
                stack.append(c)
                continue
            if not stack or stack[-1] != closedToOpen[c]:
                return False
            stack.pop()
            
        return not stack


# @lc code=end
