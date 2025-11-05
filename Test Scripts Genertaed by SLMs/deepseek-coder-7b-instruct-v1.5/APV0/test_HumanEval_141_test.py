You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_141_code import file_name_check
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_141_code import file_name_check

class TestFileNameCheck(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("example.exe"), 'Yes')
        self.assertEqual(file_name_check("example.dll"), 'Yes')
        self.assertEqual(file_name_check("a123.txt"), 'Yes')
        self.assertEqual(file_name_check("A123.exe"), 'Yes')
        self.assertEqual(file_name_check("B456.dll"), 'Yes')

    def test_invalid_file_name(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')
        self.assertEqual(file_name_check("example."), 'No')
        self.assertEqual(file_name_check("example..txt"), 'No')
        self.assertEqual(file_name_check("example.doc"), 'No')
        self.assertEqual(file_name_check("example.txt123"), 'No')
        self.assertEqual(file_name_check("example.txt1234"), 'No')
        self.assertEqual(file_name_check("example.txt12345"), 'No')
        self.assertEqual(file_name_check("example.txt123456"), 'No')
        self.assertEqual(file_name_check(""), 'No')
        self.assertEqual(file_name_check("."), 'No')
        self.assertEqual(file_name_check(".."), 'No')
        self.assertEqual(file_name_check("a."), 'No')
        self.assertEqual(file_name_check(".a"), 'No')

if __name__ == '__main__':
    unittest.main()


This script tests the `file_name_check` function with both valid and invalid file names. The `test_valid_file_name` method tests the function with valid file names and asserts that the function returns 'Yes', while the `test_invalid_file_name` method tests the function with invalid file names and asserts that the function returns 'No'.