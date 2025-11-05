You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_74_code import total_match
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    If the two lists have the same number of chars, return the first list.

    Examples:
        total_match([], []) ➞ []
        total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
        total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
        total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
        total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    l1 = 0
    for st in lst1:
        l1 += len(st)

    l2 = 0
    for st in lst2:
        l2 += len(st)

    if l1 <= l2:
        return lst1
    else:
        return lst2


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_equal_lengths(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_first_list_shorter(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_second_list_shorter(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_first_list_has_single_element(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

if __name__ == '__main__':
    unittest.main()


This script creates a class `TestTotalMatch` that inherits from `unittest.TestCase`. It includes several methods, each of which tests a different scenario. The `assertEqual` method is used to check that the output of the `total_match` function matches the expected output.

To run this script, you need to have Python installed on your machine and you need to have the `HumanEval_74_code` module available in the same directory as this script, or in a directory that's included in your Python path.

If you want to run this script directly, you need to have the `HumanEval_74_code` module available in the same directory as this script, or in a directory that's included in your Python path.

If you want to run this script directly, you can do so by running the following command in your terminal:

bash
python unittest_script.py


Replace `unittest_script.py` with the name of this script.

Please note that you need to have Python installed on your machine to run this script.