You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `parse_music` function:


import unittest
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_single_note(self):
        self.assertEqual(parse_music('o'), [4])
        self.assertEqual(parse_music('o|'), [2])
        self.assertEqual(parse_music('.|'), [1])

    def test_multiple_notes(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_notes_with_spaces(self):
        self.assertEqual(parse_music(' o o | . | o | o | . | . | . | o o '), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_notes_with_special_characters(self):
        self.assertEqual(parse_music('o!o| .#| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_notes_with_extra_spaces(self):
        self.assertEqual(parse_music('   o   o    |     .     |    o     |   o     |    .     |     .     |     .     |     .     |    o     o    '), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty string, single notes, multiple notes, notes with spaces, notes with special characters, and notes with extra spaces. It uses the `assertEqual` method to check if the output of the `parse_music` function matches the expected output for each test case.