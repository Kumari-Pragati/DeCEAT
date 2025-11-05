You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_118_code import get_closest_vowel
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if (word[i + 1] not in vowels) and (word[i - 1] not in vowels):
                return word[i]
    return ""


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_get_closest_vowel(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel(""), "")
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("b"), "")
        self.assertEqual(get_closest_vowel("aeiou"), "")
        self.assertEqual(get_closest_vowel("AEIOU"), "")
        self.assertEqual(get_closest_vowel("bcdfg"), "")
        self.assertEqual(get_closest_vowel("bcdfga"), "a")
        self.assertEqual(get_closest_vowel("bcdfgA"), "A")
        self.assertEqual(get_closest_vowel("bcdfgaeiou"), "a")
        self.assertEqual(get_closest_vowel("bcdfgaeiouA"), "A")

if __name__ == '__main__':
    unittest.main()


This script includes a unittest class `TestGetClosestVowel` with a method `test_get_closest_vowel` that tests the `get_closest_vowel` function with various inputs. Each test case checks if the function's output matches the expected output.

Please note that the `HumanEval_118_code` module should contain the `get_closest_vowel` function for these tests to pass. If the function is not in a separate module, you should replace `from HumanEval_118_code import get_closest_vowel` with `from your_script_name import get_closest_vowel`, where `your_script_name` is the name of the script that contains the `get_closest_vowel` function.