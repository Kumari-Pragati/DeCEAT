system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))


assistant

import unittest

# Importing the function from the provided code snippet
from HumanEval_16_code import count_distinct_characters

# Running the unit tests
if __name__ == '__main__':
    unittest.main()


This code snippet starts with importing the necessary module and then runs the unit tests defined in the `count_distinct_characters` function using the `unittest` framework.