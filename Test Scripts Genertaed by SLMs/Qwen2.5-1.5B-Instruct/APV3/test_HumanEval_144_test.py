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
   - Include from HumanEval_144_code import simplify
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
2. Include: from HumanEval_144_code import simplify
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator / denom == int(numerator / denom)):
        return True
    return False


assistant

import unittest

# Importing the simplified function from the given code snippet
from HumanEval_144_code import simplify

class TestSimplify(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))

    def test_edge_cases(self):
        # Edge case 1: Numerator and Denominator are equal
        self.assertTrue(simplify("2/2", "2/2"))
        
        # Edge case 2: One of the fractions has a denominator of 1
        self.assertTrue(simplify("1/3", "3/1"))
        self.assertTrue(simplify("1/4", "4/1"))
        
        # Edge case 3: One of the fractions has a numerator of 0
        self.assertFalse(simplify("0/1", "1/1"))
        self.assertFalse(simplify("0/1", "1/2"))
        
        # Edge case 4: One of the fractions has a denominator of 0
        self.assertFalse(simplify("1/0", "1/1"))
        self.assertFalse(simplify("1/0", "1/2"))

    def test_invalid_input(self):
        # Invalid input cases
        self.assertRaises(ValueError, simplify, "", "")
        self.assertRaises(ValueError, simplify, "a/b", "c/d")
        self.assertRaises(ValueError, simplify, "1/2", "b/c")

if __name__ == '__main__':
    unittest.main()