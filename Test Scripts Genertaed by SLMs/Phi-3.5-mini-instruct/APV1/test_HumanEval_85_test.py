You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_add_even_elements_at_odd_indices(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_add_empty_list(self):
        self.assertEqual(add([]), 0)

    def test_add_list_with_no_even_elements_at_odd_indices(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_list_with_even_elements_at_odd_indices(self):
        self.assertEqual(add([4, 2, 6, 8]), 10)

    def test_add_list_with_negative_numbers(self):
        self.assertEqual(add([-4, 2, -6, 8]), -4)

    def test_add_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            add([4, "2", 6, 7])

    def test_add_list_with_non_integer_elements(self):
        with self.assertRaises(ValueError):
            add([4, 2.5, 6, 7])

if __name__ == '__main__':
    unittest.main()