# Array

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
##
## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution

class TestSquaresOfASortedArray(unittest.TestCase):
    def test_sortedSquares(self):
        arr = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        result = Solution.sortedSquares(self, arr)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
```
</blockuote></details>

```python
class Solution:
    def sortedSquares(self, nums):
        res = []
        pos = 0
        length = len(nums)
        while pos < length and nums[pos] < 0:
            pos += 1
        neg = pos - 1
        while pos < length and neg >= 0:
            if -1*nums[neg] <= nums[pos]:
                res.append(nums[neg]**2)
                neg -= 1
            else:
                res.append(nums[pos]**2)
                pos += 1
        while neg >= 0:
            res.append(nums[neg]**2)
            neg -= 1
        while pos < length:
            res.append(nums[pos]**2)
            pos += 1
        return res




```