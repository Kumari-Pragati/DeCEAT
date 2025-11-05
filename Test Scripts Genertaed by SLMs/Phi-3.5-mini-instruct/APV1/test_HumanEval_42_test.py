You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]

 import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):
    def test_increment_list(self):
        # Test with a simple list
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        
        # Test with a list containing duplicates
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])
        
        # Test with an empty list
        self.assertEqual(incr_list([]), [])
        
        # Test with a list containing negative numbers
        self.assertEqual(incr_list([-1, -2, -3]), [-1, -2, -3])
        
        # Test with a list containing floating-point numbers
        self.assertEqual(incr_list([1.1, 2.2, 3.3]), [2.1, 3.2, 4.3])
        
        # Test with a list containing strings
        with self.assertRaises(TypeError):
            incr_list(["a", "b", "c"])
        
        # Test with a list containing mixed types
        with self.assertRaises(TypeError):
            incr_list([1, "a", 3.5])

if __name__ == '__main__':
    unittest.main()