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
   - Include from HumanEval_122_code import add_elements
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
2. Include: from HumanEval_122_code import add_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


assistant

import unittest

# Provided function
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):
    
    def test_normal_input(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        
    def test_edge_case_with_one_element(self):
        self.assertEqual(add_elements([1], 1), 1)
        
    def test_edge_case_with_two_elements(self):
        self.assertEqual(add_elements([1, 2], 2), 3)
        
    def test_large_number(self):
        self.assertEqual(add_elements([1000, 200, 3000, 400, 500], 5), 1000)
        
    def test_zero_sum(self):
        self.assertEqual(add_elements([], 0), 0)
        
    def test_invalid_k_value(self):
        with self.assertRaises(ValueError):
            add_elements([1, 2, 3], 0)
            
    def test_out_of_range_k_value(self):
        with self.assertRaises(IndexError):
            add_elements([1, 2, 3], 5)
            
    def test_empty_array(self):
        with self.assertRaises(AssertionError):
            add_elements([], 1)
            
    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            add_elements("not_an_array", 1)
            
    def test_floats_in_array(self):
        with self.assertRaises(TypeError):
            add_elements([1.1, 2.2, 3.3], 2)
            
    def test_string_in_array(self):
        with self.assertRaises(TypeError):
            add_elements(["a", "b", "c"], 2)
            
    def test_negative_integers(self):
        with self.assertRaises(ValueError):
            add_elements([-1, -2, -3], 3)
            
    def test_large_negative_integers(self):
        with self.assertRaises(ValueError):
            add_elements([-1000, -200, -300], 3)
            
    def test_large_positive_integers(self):
        with self.assertRaises(ValueError):
            add_elements([1000, 200, 3000, 400, 500], 5)
            
    def test_large_positive_and_negative_integers(self):
        with self.assertRaises(ValueError):
            add_elements([1000, -200, 3000, 400, -500], 5)
            
    def test_large_positive_and_negative_integers_with_k_less_than_length(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 4)
            
    def test_large_positive_and_negative_integers_with_k_greater_than_length(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 6)
            
    def test_large_positive_and_negative_integers_with_k_equal_to_length(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 5)
            
    def test_large_positive_and_negative_integers_with_k_exceeding_length(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 7)
            
    def test_large_positive_and_negative_integers_with_k_exceeding_length_minus_one(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 6)
            
    def test_large_positive_and_negative_integers_with_k_exceeding_length_plus_one(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 8)
            
    def test_large_positive_and_negative_integers_with_k_exceeding_length_plus_two(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 9)
            
    def test_large_positive_and_negative_integers_with_k_exceeding_length_plus_three(self):
        with self.assertRaises(IndexError):
            add_elements([1000, -200, 3000, 400, -500], 10)