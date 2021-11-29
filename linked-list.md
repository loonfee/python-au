# Linked List

+ [Sort List](#sort-list)
##
## Sort List

https://leetcode.com/problems/sort-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode

class TestSortList(unittest.TestCase):
    def test_merge_lists(self):
        l1 = ListNode.create_linked_list(self, [1, 3, 4])
        l2 = ListNode.create_linked_list(self, [2, 3, 6])
        expected = ListNode.create_linked_list(self, [1, 2, 3, 3, 4, 6])
        result = Solution.merge_lists(self, l1, l2)
        self.assertEqual(ListNode.get_values(self, expected), ListNode.get_values(self, result))

        
    def test_sort_List(self):
        list = ListNode.create_linked_list(self, [4, 2, 1, 3])
        expected = ListNode.create_linked_list(self, [1, 2, 3, 4])
        result = Solution.sortList(self, list)
        self.assertEqual(ListNode.get_values(self, expected), ListNode.get_values(self, result))


if __name__ == '__main__':
    unittest.main()

```
</blockuote></details>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
    def get_values(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
    
    
    def create_linked_list(self, data):
        nxt = None
        for i in range(1, len(data) + 1):
            cur = ListNode(data[-i], nxt)
            nxt = cur
        return cur

class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        l = Solution.sortList(self, head)
        r = Solution.sortList(self, slow)
        return Solution.merge_lists(self, l, r)
    
    
    def merge_lists(self, l1, l2):
        dummy = ListNode
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next




```