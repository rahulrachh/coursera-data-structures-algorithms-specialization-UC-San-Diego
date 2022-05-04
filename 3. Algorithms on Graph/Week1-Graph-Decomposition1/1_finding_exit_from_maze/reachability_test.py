import unittest
from reachability import reach


class TestStringMethods(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(reach([[1, 3], [0, 2], [1, 3], [0, 2]], 0, 3), 1, "This should be 1")
        self.assertEqual(reach([[1], [0, 2], [1], []], 0, 3), 0, "This should be 0")


if __name__ == '__main__':
    unittest.main()
