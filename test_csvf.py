import unittest
from csvf import dict_call
import pandas as pd

class TestDict(unittest.TestCase):
    def test_word(self):
        self.assertEqual(dict_call('hello'), 'hello')
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)