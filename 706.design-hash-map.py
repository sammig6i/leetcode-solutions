#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start


class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(10**4)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        cur = self.map[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self.hash(key)
        cur = self.map[idx].next

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        prev, cur = None, self.map[idx]
        while cur:
            if cur.key == key:
                prev.next = cur.next
            prev, cur = cur, cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
