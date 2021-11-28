# Linked List

+ [Middle of the Linked List](#middle-of-the-linked-list)
##
## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode

class TestMiddleOfTheLinkedList(unittest.TestCase):
    def test_middleNode(self):
        head = ListNode.create_linked_list(self, 1, 5)
        expected = ListNode.create_linked_list(self, 3, 5)
        result = Solution.middleNode(self, head)
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


    def create_linked_list(self, head_val, tail_val):
        nxt = ListNode(tail_val)
        for i in range(tail_val - 1, head_val - 1, -1):
            cur = ListNode(i, nxt)
            nxt = cur
        return cur


class Solution:
    def middleNode(self, head):
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]




```