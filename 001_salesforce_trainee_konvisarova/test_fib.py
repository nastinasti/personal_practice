import unittest
from main_process import MainProcess


class TestFileProcessing(unittest.TestCase):

    def check_fibonacci_numbers(self):
        m = MainProcess()
        self.assertFalse(m.fibonacci_check(4))
        self.assertTrue(m.fibonacci_check(5))

if __name__ == '__main__':
    unittest.main()