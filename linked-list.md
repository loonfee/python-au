# Linked List

+ [Reverse Linked List](#reverse-linked-list)
##
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode

class TestReverseLinkedListSolution(unittest.TestCase):
    def test_reverseList(self):
        tail = ListNode(2)
        head = ListNode(1, tail)
        exp_tail = ListNode(1)
        exp_head = ListNode(2, exp_tail)
        result = Solution.reverseList(self, head)
        self.assertEqual(ListNode.get_values(self, exp_head), ListNode.get_values(self, result))


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
class Solution:
    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev



```