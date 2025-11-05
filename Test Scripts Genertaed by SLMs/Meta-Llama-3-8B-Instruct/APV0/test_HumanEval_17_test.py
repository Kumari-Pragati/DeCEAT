user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_17_code import parse_music
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o'  - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]assistant

Here is the unittest test script for the `parse_music` function:

import unittest
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(parse_music('o o|.| o| o|.|.|.|.| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_empty_input(self):
        self.assertEqual(parse_music(''), [])

    def test_single_note(self):
        self.assertEqual(parse_music('o'), [4])

    def test_multiple_notes(self):
        self.assertEqual(parse_music('o o| o|'), [4, 2, 2])

    def test_invalid_input(self):
        with self.assertRaises(KeyError):
            parse_music(' invalid note ')

    def test_note_with_spaces(self):
        self.assertEqual(parse_music('o | o|'), [4, 2])

    def test_note_with_punctuation(self):
        self.assertEqual(parse_music('o! o|'), [4, 2])

    def test_note_with_multiple_punctuation(self):
        self.assertEqual(parse_music('o!| o|'), [4, 2])

if __name__ == '__main__':
    unittest.main()

This test script covers various scenarios, including:

1. Valid input with multiple notes
2. Empty input
3. Single note input
4. Multiple notes input
5. Invalid input (e.g., non-existent note)
6. Input with spaces, punctuation, and multiple punctuation

Each test case uses the `assertEqual` method to verify that the output of the `parse_music` function matches the expected result. The `assertRaises` method is used to test that the function raises a `KeyError` when given an invalid input.

You can run this script directly to execute the tests and verify that the `parse_music` function is working correctly.