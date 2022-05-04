import unittest
from max_sliding_window import max_sliding_window_naive


class TestStringMethods(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 4), [7, 7, 5, 6, 6], "This should be 7, 7, 5, 6, 6")


if __name__ == '__main__':
    unittest.main()
