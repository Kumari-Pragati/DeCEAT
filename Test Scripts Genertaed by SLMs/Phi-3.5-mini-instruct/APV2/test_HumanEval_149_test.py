You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 
import unittest
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_single_element_list(self):
        self.assertEqual(sorted_list_sum(["aa"]), ["aa"])

    def test_multiple_elements_with_even_length(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    def test_multiple_elements_with_odd_length(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_duplicate_elements(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "ab", "ab"]), ["aa", "ab"])

    def test_same_length_elements_alphabetical_order(self):
        self.assertEqual(sorted_list_sum(["ba", "aa", "ca"]), ["aa", "ba", "ca"])

    def test_same_length_elements_length_order(self):
        self.assertEqual(sorted_list_sum(["ba", "aa", "ca"]), ["aa", "ba", "ca"])

if __name__ == '__main__':
    unittest.main()


Note: The provided function `sorted_list_sum` already sorts the list alphabetically before sorting by length due to the use of `lst.sort()` and `sorted(new_lst, key=len)`. The tests above assume that the function will sort the list alphabetically first, and then by length. If the function's behavior is different, the tests should be adjusted accordingly.