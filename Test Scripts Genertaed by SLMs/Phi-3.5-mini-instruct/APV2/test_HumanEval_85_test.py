You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

 
import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_with_even_at_odd_indices(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_add_with_no_even_at_odd_indices(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_with_only_even_at_odd_indices(self):
        self.assertEqual(add([2, 4, 6, 8]), 12)

    def test_add_with_mixed_elements(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 2)

    def test_add_with_empty_list(self):
        self.assertEqual(add([]), 0)

    def test_add_with_single_element(self):
        self.assertEqual(add([2]), 0)

    def test_add_with_negative_numbers(self):
        self.assertEqual(add([-4, 2, -6, 7]), -2)

    def test_add_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            add([4, 'a', 6, 7])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `add` function, including:

- A list with even numbers at odd indices.
- A list with no even numbers at odd indices.
- A list with only even numbers at odd indices.
- A list with a mix of elements.
- An empty list.
- A list with a single element.
- A list with negative numbers.
- A list with non-integer elements to ensure proper error handling.

Each test case uses `assertEqual` to check if the output of the `add` function matches the expected result. The test suite also includes a test case to check for a `TypeError` when non-integer elements are passed to the `add` function.