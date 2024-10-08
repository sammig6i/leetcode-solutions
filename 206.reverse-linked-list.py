#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        # prev = None
        # curr = head
        # while curr:
        #     tmp = curr.next
        #     curr.next = prev
        #     prev, curr = curr, tmp
        # return prev

        # Recursive
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead


# @lc code=end
