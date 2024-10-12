#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for w, c in zip(words, pattern):
            if w in word_to_char and word_to_char[w] != c:
                return False

            if c in char_to_word and char_to_word[c] != w:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True


# @lc code=end
