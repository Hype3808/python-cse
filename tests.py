import unittest

import cse


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(cse.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
