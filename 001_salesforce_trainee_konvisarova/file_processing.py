from main_process import MainProcess


class FileProcessing:
    def __init__(self, row_numbers):
        self.input_name = 'input.txt'
        self.output_name = 'output.txt'
        self.main_ex = MainProcess()
        self.rows = row_numbers
        if type(self.rows) is str or self.rows < 0:
            raise ValueError(f'Invalid number {self.rows}')

    def input_file(self):
        count = 0
        with open(self.input_name, 'w') as file_creator:
            while count < self.rows:
                file_creator.write(f'raw {count + 1}\n')
                count += 1

    def get_data_from_file(self):
        result = list()
        count = 1
        try:
            with open(self.input_name, 'r') as input_f:
                while count <= self.rows:
                    file_string = f'{self.main_ex.reverse_row(input_f.readline().strip())}\n'
                    if self.main_ex.fibonacci_check(count):
                        result.append(file_string)
                    count += 1
        except IOError:
            raise IOError('File is not available')
        return result

    def output_file(self):
        with open(self.output_name, 'w') as file_output:
            for strings in self.get_data_from_file():
                file_output.write(strings)


