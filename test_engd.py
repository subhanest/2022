import unittest
from engd import callup
import json

class TestDict(unittest.TestCase):
    def test_word(self):
        self.assertEqual(callup(34), 200)
    
if __name__ == "__main__":
    unittest.main()

    