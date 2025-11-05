You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_113_code import odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3', "11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """

    res = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        res.append(
            "the number of odd elements "
            + str(n)
            + "n the str"
            + str(n)
            + "ng "
            + str(n)
            + " of the "
            + str(n)
            + "nput."
        )
    return res

 Here is the complete unittest test suite for the `odd_count` function:


import unittest
from HumanEval_113_code import odd_count

class TestOddCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(odd_count([]), [])

    def test_single_element_list(self):
        self.assertEqual(
            odd_count(['1234567']),
            ["the number of odd elements 4n the str4ng 4 of the 4nput."]
        )

    def test_multiple_elements_list(self):
        self.assertEqual(
            odd_count(['3', "11111111"]),
            ["the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 8n the str8ng 8 of the 8nput."]
        )

    def test_mixed_numbers_list(self):
        self.assertEqual(
            odd_count(['1', '3', '5', '7', '9', '11', '13', '15', '17']),
            ["the number of odd elements 1n the str1ng 1 of the 1nput.",
             "the number of odd elements 1n the str3 of the 1nput.",
             "the number of odd elements 1n the str5 of the 1nput.",
             "the number of odd elements 1n the str7 of the 1nput.",
             "the number of odd elements 1n the str9 of the 1nput.",
             "the number of odd elements 1n the str11 of the 1nput.",
             "the number of odd elements 1n the str13 of the 1nput.",
             "the number of odd elements 1n the str15 of the 1nput.",
             "the number of odd elements 1n the str17 of the 1nput."]
        )

    def test_all_even_numbers_list(self):
        self.assertEqual(
            odd_count(['2', '4', '6', '8', '0']),
            ["the number of odd elements 0n the str2 of the 0nput.",
             "the number of odd elements 0n the str4 of the 0nput.",
             "the number of odd elements 0n the str6 of the 0nput.",
             "the number of odd elements 0n the str8 of the 0nput.",
             "the number of odd elements 0n the str0 of the 0nput."]
        )

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, a single-element list, a list with multiple elements, a list with mixed numbers, and a list with all even numbers.