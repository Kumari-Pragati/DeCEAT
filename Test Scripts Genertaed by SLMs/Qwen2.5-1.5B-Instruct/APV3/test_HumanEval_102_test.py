system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_102_code import choose_num
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_102_code import choose_num
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


assistant

import unittest

from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(choose_num(12, 15), 14)
    
    def test_edge_case_1(self):
        self.assertEqual(choose_num(13, 12), -1)
    
    def test_edge_case_2(self):
        self.assertEqual(choose_num(12, 12), 12)
    
    def test_edge_case_3(self):
        self.assertEqual(choose_num(13, 13), -1)
    
    def test_invalid_input(self):
        self.assertEqual(choose_num(-1, 5), -1)
        self.assertEqual(choose_num(5, -1), -1)
        self.assertEqual(choose_num(0, 0), -1)
        self.assertEqual(choose_num(1, 1), -1)
        self.assertEqual(choose_num(1, 2), -1)
        self.assertEqual(choose_num(2, 1), -1)
        self.assertEqual(choose_num(2, 2), 2)
        self.assertEqual(choose_num(2, 3), 2)
        self.assertEqual(choose_num(3, 2), -1)
        self.assertEqual(choose_num(3, 3), 3)
        self.assertEqual(choose_num(3, 4), 4)
        self.assertEqual(choose_num(4, 3), -1)
        self.assertEqual(choose_num(4, 4), 4)
        self.assertEqual(choose_num(4, 5), 4)
        self.assertEqual(choose_num(5, 4), -1)
        self.assertEqual(choose_num(5, 5), 5)
        self.assertEqual(choose_num(5, 6), 6)
        self.assertEqual(choose_num(6, 5), -1)
        self.assertEqual(choose_num(6, 6), 6)
        self.assertEqual(choose_num(6, 7), 6)
        self.assertEqual(choose_num(7, 6), -1)
        self.assertEqual(choose_num(7, 7), 7)
        self.assertEqual(choose_num(7, 8), 8)
        self.assertEqual(choose_num(8, 7), -1)
        self.assertEqual(choose_num(8, 8), 8)
        self.assertEqual(choose_num(8, 9), 8)
        self.assertEqual(choose_num(9, 8), -1)
        self.assertEqual(choose_num(9, 9), 9)
        self.assertEqual(choose_num(9, 10), 10)
        self.assertEqual(choose_num(10, 9), -1)
        self.assertEqual(choose_num(10, 10), 10)
        self.assertEqual(choose_num(10, 11), 10)
        self.assertEqual(choose_num(11, 10), -1)
        self.assertEqual(choose_num(11, 11), 11)
        self.assertEqual(choose_num(11, 12), 12)
        self.assertEqual(choose_num(12, 11), -1)
        self.assertEqual(choose_num(12, 12), 12)
        self.assertEqual(choose_num(12, 13), 12)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(13, 13), 13)
        self.assertEqual(choose_num(13, 14), 14)
        self.assertEqual(choose_num(14, 13), -1)
        self.assertEqual(choose_num(14, 14), 14)
        self.assertEqual(choose_num(14, 15), 14)
        self.assertEqual(choose_num(15, 14), -1)
        self.assertEqual(choose_num(15, 15), 15)
        self.assertEqual(choose_num(15, 16), 16)
        self.assertEqual(choose_num(16, 15), -1)
        self.assertEqual(choose_num(16, 16), 16)
        self.assertEqual(choose_num(16, 17), 16)
        self.assertEqual(choose_num(17, 16), -1)
        self.assertEqual(choose_num(17, 17), 17)
        self.assertEqual(choose_num(17, 18), 18)
        self.assertEqual(choose_num(18, 17), -1)
        self.assertEqual(choose_num(