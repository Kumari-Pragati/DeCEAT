system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]


assistant

import unittest

# Define the function to be tested
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):
    def test_parse_music(self):
        # Test case 1: Whole notes
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

        # Test case 2: Half notes
        self.assertEqual(parse_music('o| .|. o| .| o| .| .| .| o o'), [2, 1, 2, 1, 1, 1, 1, 1, 4, 4])

        # Test case 3: Quarter notes
        self.assertEqual(parse_music('.| .|. o| .| .| .| .| o o'), [1, 1, 2, 1, 1, 1, 1, 1, 4, 4])

        # Test case 4: Mixed notes (should raise an error)
        try:
            parse_music('o o| .| o| o| .| .| .| .| o o|')
        except ValueError as e:
            self.assertTrue(str(e).startswith("Invalid input"))

if __name__ == '__main__':
    unittest.main()


This script defines a `TestParseMusic` class that inherits from `unittest.TestCase`. It contains several test cases using assertEqual methods to verify that the `parse_music` function returns the expected results. The `try-except` block is used to handle invalid inputs gracefully. Finally, the `unittest.main()` call at the end makes the tests executable when run directly.