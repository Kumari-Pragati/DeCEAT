user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_152_code import compare
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def compare(game, guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(x - y) for x, y in zip(game, guess)]assistant

Here is the unittest test script for the `compare` function:

import unittest
from HumanEval_152_code import compare

class TestCompareFunction(unittest.TestCase):
    def test_compare_correct_guess(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        expected_result = [0, 0, 0, 0, 3, 3]
        self.assertEqual(compare(game, guess), expected_result)

    def test_compare_incorrect_guess(self):
        game = [0, 5, 0, 0, 0, 4]
        guess = [4, 1, 1, 0, 0, -2]
        expected_result = [4, 4, 1, 0, 0, 6]
        self.assertEqual(compare(game, guess), expected_result)

    def test_compare_empty_game_and_guess(self):
        game = []
        guess = []
        expected_result = []
        self.assertEqual(compare(game, guess), expected_result)

    def test_compare_game_and_guess_of_different_lengths(self):
        game = [1, 2, 3]
        guess = [1, 2, 3, 4]
        with self.assertRaises(IndexError):
            compare(game, guess)

    def test_compare_game_and_guess_with_non_integer_values(self):
        game = [1, 2, 3, 4, 5, 1.5]
        guess = [1, 2, 3, 4, 2, -2]
        with self.assertRaises(TypeError):
            compare(game, guess)

if __name__ == '__main__':
    unittest.main()

This script tests the `compare` function with various inputs, including:

1. Correct guesses
2. Incorrect guesses
3. Empty game and guess arrays
4. Game and guess arrays of different lengths (to test for IndexError)
5. Game and guess arrays with non-integer values (to test for TypeError)

Each test case uses the `assertEqual` method to check that the output of the `compare` function matches the expected result. If the output does not match the expected result, the test will fail and an error message will be displayed.