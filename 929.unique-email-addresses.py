#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            i = 0
            local = ""
            while email[i] != "@":
                if email[i] == ".":
                    i += 1
                elif email[i] == "+":
                    break
                else:
                    local += email[i]
                    i += 1
            
            while email[i] != "@":
                i += 1
            
            domain = email[i:]

            res.add(local + domain)
        return len(res)
            



# @lc code=end
