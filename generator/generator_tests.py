import unittest
import perevod as gnr

class TestGenerator(unittest.TestCase):
    def test_get_new_md_solution(self):
        file_content = 'Two Sum\n' \
                       'https://leetcode.com/problems/two-sum/\n' \
                       'class Solution(object):\n' \
                       '    def twoSum(self, nums, target):\n' \
                       '        previous_nums = {}\n' \
                       '        for index, num in enumerate(nums):\n' \
                       '            diff = target - num\n' \
                       '            if(diff in previous_nums):\n' \
                       '                return index, previous_nums[diff]\n' \
                       '            previous_nums[num] = index'
        expected = {'md_link': '+ [Two Sum](#two-sum)',
                    'md_solution': '## Two Sum\n'
                    '\n'
                    'https://leetcode.com/problems/two-sum/\n'
                    '\n'
                    '```python\n'
                    'class Solution(object):\n'
                    '    def twoSum(self, nums, target):\n'
                    '        previous_nums = {}\n'
                    '        for index, num in enumerate(nums):\n'
                    '            diff = target - num\n'
                    '            if(diff in previous_nums):\n'
                    '                return index, previous_nums[diff]\n'
                    '            previous_nums[num] = index\n'
                    '\n'
                    '```'}
        self.assertEqual(expected, gnr.get_new_md_solution(file_content))


    def test_get_old_md_solutions(self):
        file_content = '+ [Two Sum](#two-sum)' \
                       '\n' \
                       '+ [Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)' \
                       '## Two Sum\n' \
                       '\n' \
                       'https://leetcode.com/problems/two-sum/\n' \
                       '\n' \
                       '```python\n' \
                       'class Solution(object):\n' \
                       '    def twoSum(self, nums, target):\n' \
                       '        previous_nums = {}\n' \
                       '        for index, num in enumerate(nums):\n' \
                       '            diff = target - num\n' \
                       '            if(diff in previous_nums):\n' \
                       '                return index, previous_nums[diff]\n' \
                       '            previous_nums[num] = index\n' \
                       '\n' \
                       '```' \
                       '\n' \
                       '## Longest Substring Without Repeating Characters\n' \
                       '\n' \
                       'https://leetcode.com/problems/longest-substring-without-repeating-characters/\n' \
                       '\n' \
                       '```python\n' \
                       'class Solution(object):\n' \
                       'def lengthOfLongestSubstring(self, s):\n' \
                       'res = 0\n' \
                       'l = 0\n' \
                       'r = 0\n' \
                       'ch_set = set()\n' \
                       'length = len(s)\n' \
                       'for r in range(length):\n' \
                           'while(s[r] in ch_set):\n' \
                               'ch_set.remove(s[l])\n' \
                               'l+= 1\n' \
                          'ch_set.add(s[r])\n' \
                       'res = max(res, r - l + 1)\n' \
                      'return res\n' \
                      '\n' \
                      '```'
        expected = {'md_links': '+ [Two Sum](#two-sum)'
                                '\n'
                                '+ [Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)',
                    'md_solutions':
                       '## Two Sum\n' \
                       '\n' \
                       'https://leetcode.com/problems/two-sum/\n' \
                       '\n' \
                       '```python\n' \
                       'class Solution(object):\n' \
                       '    def twoSum(self, nums, target):\n' \
                       '        previous_nums = {}\n' \
                       '        for index, num in enumerate(nums):\n' \
                       '            diff = target - num\n' \
                       '            if(diff in previous_nums):\n' \
                       '                return index, previous_nums[diff]\n' \
                       '            previous_nums[num] = index\n' \
                       '\n' \
                       '```' \
                       '\n' \
                       '## Longest Substring Without Repeating Characters\n' \
                       '\n' \
                       'https://leetcode.com/problems/longest-substring-without-repeating-characters/\n' \
                       '\n' \
                       '```python\n' \
                       'class Solution(object):\n' \
                       'def lengthOfLongestSubstring(self, s):\n' \
                       'res = 0\n' \
                       'l = 0\n' \
                       'r = 0\n' \
                       'ch_set = set()\n' \
                       'length = len(s)\n' \
                       'for r in range(length):\n' \
                           'while(s[r] in ch_set):\n' \
                               'ch_set.remove(s[l])\n' \
                               'l+= 1\n' \
                          'ch_set.add(s[r])\n' \
                       'res = max(res, r - l + 1)\n' \
                      'return res\n' \
                      '\n' \
                      '```'}
        self.assertEqual(expected, gnr.get_old_md_solutions(file_content))


    def test_get_new_md_content(self):
        file_content_old = {'md_links': '+ [Two Sum](#two-sum)',
                    'md_solutions': '## Two Sum\n'
                    '\n'
                    'https://leetcode.com/problems/two-sum/\n'
                    '\n'
                    '```python\n'
                    'class Solution(object):\n'
                    '    def twoSum(self, nums, target):\n'
                    '        previous_nums = {}\n'
                    '        for index, num in enumerate(nums):\n'
                    '            diff = target - num\n'
                    '            if(diff in previous_nums):\n'
                    '                return index, previous_nums[diff]\n'
                    '            previous_nums[num] = index\n'
                    '\n'
                    '```'}
        file_content_new = {'md_link': '+ [Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)',
                    'md_solution': '## Longest Substring Without Repeating Characters\n' \
                    '\n' \
                    'https://leetcode.com/problems/longest-substring-without-repeating-characters/\n' \
                    '\n' \
                    '```python\n' \
                    'class Solution(object):\n' \
                        'def lengthOfLongestSubstring(self, s):\n' \
                        'res = 0\n' \
                        'l = 0\n' \
                        'r = 0\n' \
                        'ch_set = set()\n' \
                        'length = len(s)\n' \
                        'for r in range(length):\n' \
                            'while(s[r] in ch_set):\n' \
                                 'ch_set.remove(s[l])\n' \
                                 'l+= 1\n' \
                            'ch_set.add(s[r])\n' \
                        'res = max(res, r - l + 1)\n' \
                        'return res\n' \
                    '\n' \
                    '```'
                     }
        expected = '+ [Two Sum](#two-sum)' \
                    '\n' \
                    '+ [Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)' \
                    '\n'\
                    '## Two Sum\n' \
                    '\n' \
                    'https://leetcode.com/problems/two-sum/\n' \
                    '\n' \
                    '```python\n' \
                    'class Solution(object):\n' \
                    '    def twoSum(self, nums, target):\n' \
                    '        previous_nums = {}\n' \
                    '        for index, num in enumerate(nums):\n' \
                    '            diff = target - num\n' \
                    '            if(diff in previous_nums):\n' \
                    '                return index, previous_nums[diff]\n' \
                    '            previous_nums[num] = index\n' \
                    '\n' \
                    '```' \
                    '\n' \
                    '## Longest Substring Without Repeating Characters\n' \
                    '\n' \
                    'https://leetcode.com/problems/longest-substring-without-repeating-characters/\n' \
                    '\n' \
                    '```python\n' \
                    'class Solution(object):\n' \
                        'def lengthOfLongestSubstring(self, s):\n' \
                        'res = 0\n' \
                        'l = 0\n' \
                        'r = 0\n' \
                        'ch_set = set()\n' \
                        'length = len(s)\n' \
                        'for r in range(length):\n' \
                            'while(s[r] in ch_set):\n' \
                                 'ch_set.remove(s[l])\n' \
                                 'l+= 1\n' \
                            'ch_set.add(s[r])\n' \
                        'res = max(res, r - l + 1)\n' \
                        'return res\n' \
                    '\n' \
                    '```'
        self.assertEqual(expected, gnr.get_new_md_content(file_content_old, file_content_new))

if __name__ == '__main__':
    unittest.main()
