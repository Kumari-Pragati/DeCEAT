You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_95_code import check_dict_case

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    
    Examples:
    check_dict_case({"a": "apple", "b": "banana"}) -> True
    check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) -> False
    check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) -> False
    check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) -> False
    check_dict_case({"STATE": "NC", "ZIP": "12345"}) -> True
    """

    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():
            if not isinstance(key, str):
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                state = "mixed"
                break
            else:
                break
        return state == "upper" or state == "lower"

 Here is a comprehensive unittest test suite for the given Python function `check_dict_case`. The test cases cover various scenarios to ensure the function works as expected.


import unittest
from HumanEval_95_code import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

    def test_lowercase_dict(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_mixed_case_dict(self):
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))

    def test_non_string_key(self):
        self.assertFalse(check_dict_case({"a": "apple", 8: "banana"}))

    def test_multiple_lowercase_keys(self):
        self.assertFalse(check_dict_case({"a": "apple", "a": "orange"}))

    def test_multiple_uppercase_keys(self):
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

    def test_mixed_case_values(self):
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty dictionary, lowercase keys, mixed case keys, non-string keys, multiple keys with the same lowercase string, multiple keys with the same uppercase string, and mixed case values.