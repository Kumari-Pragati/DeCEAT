user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_20_code import find_closest_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """From a supplied list of numbers (of length at least two), select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx!= idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pairassistant

Here is the unittest test script for the `find_closest_elements` function:

import unittest
from HumanEval_20_code import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    def test_closest_elements(self):
        # Test case 1: Simple case with two closest elements
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

        # Test case 2: Simple case with identical elements
        self.assertEqual(find_closest_elements([1.0, 2.0, 2.0, 3.0, 4.0, 5.0]), (2.0, 2.0))

        # Test case 3: Edge case with only two elements
        self.assertEqual(find_closest_elements([1.0, 2.0]), (1.0, 2.0))

        # Test case 4: Edge case with only three elements
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0]), (2.0, 2.0))

        # Test case 5: Edge case with all identical elements
        self.assertEqual(find_closest_elements([1.0, 1.0, 1.0, 1.0, 1.0]), (1.0, 1.0))

        # Test case 6: Edge case with negative numbers
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]), (-2.0, -2.2))

        # Test case 7: Edge case with mixed positive and negative numbers
        self.assertEqual(find_closest_elements([-1.0, 2.0, -2.0, 3.0, -3.0, 2.2]), (-2.0, -2.0))

    def test_invalid_input(self):
        # Test case 8: Empty list
        with self.assertRaises(IndexError):
            find_closest_elements([])

        # Test case 9: List with less than two elements
        with self.assertRaises(IndexError):
            find_closest_elements([1.0])

if __name__ == '__main__':
    unittest.main()

This test script covers various edge cases, including:

* Simple cases with two closest elements
* Identical elements
* Edge cases with only two, three, or all identical elements
* Edge cases with negative numbers
* Mixed positive and negative numbers
* Invalid input cases (empty list or list with less than two elements)

Note that the `unittest` framework provides a `assertRaises` method to test that a specific exception is raised when an invalid input is provided.