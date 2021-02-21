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

if __name__ == '__main__':
    unittest.main()