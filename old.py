import hashlib
import os
from pathlib import Path

COLUMNS_IN_ROW = 3
HASH_TYPE = ['md5', 'sha1', 'sha256']


class CheckHash:
    def __init__(self, path_main_file, path_for_files):
        self.path_input_file = self.create_path(path_main_file)
        self.path_to_files = self.create_path(path_for_files)

    @staticmethod
    def create_path(path):
        """
        If this folder then adds a '/'
        :param path: the path to the file
        :return: path
        """
        if path == '':
            return path
        elif list(path)[-1] != '/' and len(path.split('.')) < 2:
            return path + '/'
        else:
            return path

    def validation_line_in_file(self, line, num_line):
        """
        Checks line in an open file for correctness
        :param line: the line in an open file
        :param num_line: line index
        :return: True or termination of the program
        """
        separate_line = line.split(' ', maxsplit=COLUMNS_IN_ROW)
        file = self.path_to_files + separate_line[0]

        if len(separate_line) != COLUMNS_IN_ROW:
            """ Check the allowed number of columns in a row"""
            print(f"Invalid string \n--- {line} ---\n in line {num_line}. Count columns must be: {COLUMNS_IN_ROW}")
            return 'exit'

        if separate_line[1].lower() not in HASH_TYPE:
            """ Check if the hash name is in the available list """
            print(
                f"\nInvalid encoding method: {separate_line[1].lower()}\n--- {line} ---\nin line {num_line}"
                f". Available encoding: {HASH_TYPE}")
            return 'exit'

        if len(separate_line[0].split('.')) < 2 or separate_line[0].split('.')[0] == '':
            """ Check the filename and extension"""
            print(f"File name error \n--- {line} ---\n in line {num_line}. Check the filename: {separate_line[0]}")
            return 'exit'
        else:
            if not os.path.exists(file):
                """ Check available file"""
                print(f'{file} NOT FOUND')
                return 'continua'

        return True

    def check_hash(self, obj):
        """
        Check if hash sums match
        :param obj: the line in an open file
        :return: <filename> OK or NOT
        """
        separate_line = obj.split(' ')
        hash_type = separate_line[1].lower()
        hash_sum_provided = separate_line[2]
        file = self.path_to_files + separate_line[0]

        if hash_type in (HASH_TYPE and hashlib.algorithms_available):
            hash_sum_received = hashlib.new(hash_type, file.encode()).hexdigest()
            if hash_sum_provided == hash_sum_received:
                print(f'{file} OK')
            elif os.path.exists(file):
                print(f'{file} FAIL')
        else:
            print(f'This type "{hash_type}" is not supported')
            exit()

    def read_file(self):
        """
        Opens a file for reading
        :return: None
        """
        try:
            if Path(self.path_input_file).stat().st_size == 0:
                print(f"File {self.path_input_file} empty")
                exit()

            with open(self.path_input_file, "r") as f:
                for num, line in enumerate(f, 1):
                    if len(line.split()) == 0:
                        continue
                    str_line = line.replace('\n', '')
                    if not self.validation_line_in_file(str_line, num):
                        exit()
                    else:
                        self.check_hash(str_line)

        except FileNotFoundError:
            print(f"File {self.path_input_file} not found")
        except IOError:
            print(f'File {self.path_input_file} not available')


def check_exists_file(value):
    """
    Checks the file path.
    :param value: the path to the file
    :return: Bool
    """
    if len(value) == 0 or len(value.split('.')) < 2:
        print('You didn`t specify the file path. Try it again ')
        return True
    elif not os.path.exists(value):
        print('File on the given path was not found. Check path')
        return True


if __name__ == '__main__':
    path_input_file = input('Path to the input file:\n')
    while check_exists_file(path_input_file):
        path_input_file = input(f'Path to the input file:\n')

    path_to_files = input('Path to the directory containing the files to check:\n')

    ch = CheckHash(path_input_file, path_to_files)
    ch.read_file()
