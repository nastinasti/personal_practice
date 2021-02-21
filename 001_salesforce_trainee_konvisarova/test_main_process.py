import unittest
from main_process import MainProcess

m = MainProcess()

class TestFileProcessing(unittest.TestCase):

    def test_check_fibonacci_numbers(self):
        self.assertFalse(m.fibonacci_check(4))
        self.assertTrue(m.fibonacci_check(5))

    def test_check_perfect_square(self):
        self.assertFalse(m.perfectSquare(-1))
        self.assertEqual(m.perfectSquare(10), 100)

    def test_reverse_string(self):
        self.assertEqual(m.reverse_row('Hello World'), 'dlroW olleH')
        self.assertEqual(m.reverse_row('123456'), '654321')


if __name__ == '__main__':
    unittest.main()