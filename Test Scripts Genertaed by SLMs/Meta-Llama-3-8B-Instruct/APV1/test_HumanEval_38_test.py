user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_38_code import decode_cyclic
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups, each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group, unless the group has fewer than 3 elements.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function.
    Returns decoded string.
    """
    return encode_cyclic(encode_cyclic(s))assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_38_code import decode_cyclic, encode_cyclic

class TestEncodeCyclic(unittest.TestCase):

    def test_encode_cyclic_empty_string(self):
        self.assertEqual(encode_cyclic(""), "")

    def test_encode_cyclic_single_char(self):
        self.assertEqual(encode_cyclic("a"), "a")

    def test_encode_cyclic_three_chars(self):
        self.assertEqual(encode_cyclic("abc"), "cab")

    def test_encode_cyclic_multiple_of_three_chars(self):
        self.assertEqual(encode_cyclic("abcabc"), "cabcab")

    def test_encode_cyclic_multiple_of_three_chars_with_spaces(self):
        self.assertEqual(encode_cyclic("abc def"), "fedabc def")

    def test_encode_cyclic_non_multiple_of_three_chars(self):
        self.assertEqual(encode_cyclic("abcd"), "cdabc")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces(self):
        self.assertEqual(encode_cyclic("abc defg"), "fedgabc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation(self):
        self.assertEqual(encode_cyclic("abc def,ghi"), "fed,ghiabc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers(self):
        self.assertEqual(encode_cyclic("abc def,ghi123"), "fed,ghi123abc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@#"), "fed,ghi123!@#abc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n"), "fed,ghi123!@# \nabc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n\t"), "fed,ghi123!@# \n\tabc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab_and_carriage_return(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n\t\r"), "fed,ghi123!@# \n\t\rabc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab_and_carriage_return_and_backslash(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n\t\r\\"), "fed,ghi123!@# \n\t\r\\abc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab_and_carriage_return_and_backslash_and_colon(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n\t\r\\:"), "fed,ghi123!@# \n\t\r\\:abc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n\t\r\\:,"), "fed,ghi123!@# \n\t\r\\:,abc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma_and_semicolon(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n\t\r\\:,;"), "fed,ghi123!@# \n\t\r\\:,;abc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma_and_semicolon_and_question_mark(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n\t\r\\:,;?"), "fed,ghi123!@# \n\t\r\\:,;?abc def")

    def test_encode_cyclic_non_multiple_of_three_chars_with_spaces_and_punctuation_and_numbers_and_special_chars_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma_and_semicolon_and_question_mark_and_exclamation_mark(self):
        self.assertEqual(encode_cyclic("abc def,ghi123!@# \n