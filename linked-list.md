# Linked List

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
##
## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode

class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def test_getIntersectionNode(self):
        expected = ListNode.create_linked_list(self, [3, 7])
        l1 = ListNode.create_linked_list(self, [1])
        l1.next = expected
        l2 = ListNode.create_linked_list(self, [2, 4])
        l2.next = expected
        result = Solution.getIntersectionNode(self, l1, l2)
        self.assertEqual(ListNode.get_values(self, expected), ListNode.get_values(self, result))
    def test_getIntersectionNode(self):
        expected = None
        l1 = ListNode.create_linked_list(self, [1, 2])
        l2 = ListNode.create_linked_list(self, [3, 4])
        result = Solution.getIntersectionNode(self, l1, l2)
        self.assertEqual(expected, result)


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
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while(a!=b):
            if (a):
                a = a.next
            else:
                a = headB
            if (b):
                b = b.next
            else:
                b = headA
        return a







```