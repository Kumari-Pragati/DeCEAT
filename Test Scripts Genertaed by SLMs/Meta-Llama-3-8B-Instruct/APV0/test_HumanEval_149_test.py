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
    return sorted(new_lst, key=len)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_sorted_list_sum(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])
        self.assertEqual(sorted_list_sum(["abc", "ab", "abcd", "def"]), ["ab", "abc", "abcd", "def"])
        self.assertEqual(sorted_list_sum(["a", "b", "c", "d"]), ["a", "b", "c", "d"])
        self.assertEqual(sorted_list_sum(["a", "b", "c", "d", "e", "f", "g", "h", "i"]), ["a", "b", "c", "d", "e", "f", "g", "h", "i"])
        self.assertEqual(sorted_list_sum(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"])
        self.assertEqual(sorted_list_sum(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"])

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_single_element_list(self):
        self.assertEqual(sorted_list_sum(["a"]), ["a"])

    def test_list_with_duplicates(self):
        self.assertEqual(sorted_list_sum(["a", "a", "b", "b", "c", "c"]), ["a", "a", "b", "b", "c", "c"])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function is working correctly. The test cases cover various scenarios, including lists with different lengths, empty lists, lists with duplicates, and lists with single elements.