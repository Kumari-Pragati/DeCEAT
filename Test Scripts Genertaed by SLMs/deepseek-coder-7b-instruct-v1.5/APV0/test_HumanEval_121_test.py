You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5]), 3)
        self.assertEqual(solution([10, 9, 8, 7, 6]), 9)
        self.assertEqual(solution([1, 3, 5, 7, 9]), 0)
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 8, 10]), 8)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestSolution` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_solution` that tests the `solution` function with various inputs. Each `self.assertEqual` call checks if the output of the `solution` function is as expected.

The script ends with `unittest.main()`, which runs all the tests when the script is run directly.

Please note that you need to have the `HumanEval_121_code` module and the `solution` function defined in that module for this script to work. If the `solution` function is defined in a different module, you need to replace `from HumanEval_121_code import solution` with the appropriate import statement.