from file_processing import FileProcessing

if __name__ == '__main__':
    rows_number = int(input("Please enter the number of rows: \n"))
    file_p = FileProcessing(rows_number)
    file_p.input_file()
    file_p.output_file()