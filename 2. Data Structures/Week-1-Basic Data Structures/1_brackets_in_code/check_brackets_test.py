import unittest
from check_brackets import find_mismatch

class TestStringMethods(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(find_mismatch('[]'), 'Success', "This should be 'Success'")
        self.assertEqual(find_mismatch('{}[]'), 'Success', "This should be 'Success'")
        self.assertEqual(find_mismatch('[()]'), 'Success', "This should be 'Success'")
        self.assertEqual(find_mismatch('(())'), 'Success', "This should be 'Success'")
        self.assertEqual(find_mismatch('{[]}()'), 'Success', "This should be 'Success'")
        self.assertEqual(find_mismatch('{'), 1, "This should be 1")
        self.assertEqual(find_mismatch('{[}'), 3, "This should be 3")
        self.assertEqual(find_mismatch('foo(bar);'), 'Success', "This should be 'Success'")
        self.assertEqual(find_mismatch('foo(bar[i);'), 10, "This should be 10")


if __name__ == '__main__':
    unittest.main()
