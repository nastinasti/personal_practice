

class MainProcess:

    def fibonacci_check(self, row_number):
        return self.perfectSquare(5*(row_number**2) + 4) or self.perfectSquare(5*(row_number**2) - 4)

    def perfectSquare(self, n):
        try:
            res = int(n ** (1/2))
            return res * res == n
        except TypeError:
            raise TypeError('The number is not valid')

    def reverse_row(self, row_string):
        return row_string[::-1]
