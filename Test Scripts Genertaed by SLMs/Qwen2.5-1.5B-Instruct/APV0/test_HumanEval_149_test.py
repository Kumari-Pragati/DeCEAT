system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_149_code import sorted_list_sum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


assistant

import unittest

# Function to be tested
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_sorted_list_sum(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])
        self.assertEqual(sorted_list_sum(["hello", "world", "hi", "earth"]), ["hello", "world", "hi"])
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["apple", "banana", "cherry"])

if __name__ == '__main__':
    unittest.main()


This script defines a `TestSortedListSum` class within the `unittest` module, which contains a single method `test_sorted_list_sum`. This method tests the `sorted_list_sum` function using several assertions based on provided examples. When run, this script will execute these tests and verify that the function behaves as expected.