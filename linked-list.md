# Linked List

+ [Palindrome Linked List](#palindrome-linked-list)
##
## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode

class TestPalindromeLinkedList(unittest.TestCase):
    def test_isPalindrome(self):
        head = ListNode.create_linked_list(self, [1, 2, 3])
        expected = 0
        result = Solution.isPalindrome(self, head)
        self.assertEqual(expected, result)


    def test_isPalindrome(self):
        head = ListNode.create_linked_list(self, [1, 2, 1])
        expected = 1
        result = Solution.isPalindrome(self, head)
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


    def create_linked_list(self, data):
        nxt = None
        for i in range(1, len(data) + 1):
            cur = ListNode(data[-i], nxt)
            nxt = cur
        return cur

    
class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        l, r = head, prev
        while r:
            if l.val != r.val:
                return 0
            l = l.next
            r = r.next
        return 1




```