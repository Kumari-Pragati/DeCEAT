Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_121_code import solution
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])

 Here is a unittest test script for the provided function:


import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5]), 6)
        self.assertEqual(solution([-1, 2, -3, 4, -5]), 2)
        self.assertEqual(solution([0, 1, 2, 3, 4]), 2)
        self.assertEqual(solution([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([2, 4, 6]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9]), 20)

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases to ensure the function works correctly for various inputs. It covers the edge cases of empty lists, lists containing only even or odd numbers, and lists with both even and odd numbers. The test cases are designed to cover the conditions specified in the function description.