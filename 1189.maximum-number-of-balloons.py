#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start


from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letterCount = Counter(text)
        balloonCount = Counter("balloon")

        res = float("inf")
        for c in balloonCount:
            res = min(letterCount[c] // balloonCount[c], res)
        return res


# @lc code=end
