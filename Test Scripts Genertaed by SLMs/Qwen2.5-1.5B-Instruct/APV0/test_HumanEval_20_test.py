system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair


assistant

import unittest

# Importing the function we want to test
from HumanEval_20_code import find_closest_elements

class TestFindClosestElements(unittest.TestCase):

    def test_find_closest_elements(self):
        # Test case 1
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        self.assertEqual(result, (2.0, 2.2))

        # Test case 2
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        self.assertEqual(result, (2.0, 2.0))

        # Test case 3
        result = find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -6.0])
        self.assertEqual(result, (-2.0, -2.0))

        # Test case 4
        result = find_closest_elements([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(result, (1.0, 2.0))

        # Test case 5
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        self.assertEqual(result, (2.0, 2.0))

        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This script imports the `find_closest_elements` function and defines a class `TestFindClosestElements` within a unit testing framework called `unittest`. It contains several test cases to ensure the function behaves as expected under different scenarios. The `assertEqual` method checks if the output matches the expected results. If all tests pass, it prints "All tests passed!" to indicate successful execution.