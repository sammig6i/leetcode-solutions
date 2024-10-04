#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    res = a + b
                    stack.append(res)
                elif t == "-":
                    res = a - b
                    stack.append(res)
                elif t == "*":
                    res = a * b
                    stack.append(res)
                elif t == "/":
                    res = int(a / b)
                    stack.append(res)
            else:
                stack.append(int(t))

        return stack[-1]


# @lc code=end
