import hashlib
import os

COLUMNS_IN_ROW = 3
HASH_TYPE = ['md5', 'sha1', 'sha256']


class CheckHash:
    def __init__(self, path_main_file, path_for_files):
        self.path_input_file = self.__create_path(path_main_file)
        self.path_to_files = self.__create_path(path_for_files)

    @staticmethod
    def __create_path(path):
        if path == '':
            return path
        elif list(path)[-1] != '/' and len(path.split('.')) < 2:
            return path + '/'
        else:
            return path

    def _validation_line_in_file(self, line, num_line):
        separate_line = line.split(' ', maxsplit=COLUMNS_IN_ROW)
        file = self.path_to_files + separate_line[0]
        if len(separate_line) != COLUMNS_IN_ROW:
            """ Check the allowed number of columns in a row"""
            print(f"Invalid string \n--- {line} ---\n in line {num_line}. Max count columns: {COLUMNS_IN_ROW}")
            exit()
        else:
            if separate_line[1].lower() not in HASH_TYPE:
                """ Check if the hash name is in the available list """
                print(
                    f"\nInvalid encoding method: {separate_line[1].lower()}\n--- {line} ---\nin line {num_line}. Available encoding: {HASH_TYPE}")
                exit()

            if len(separate_line[0].split('.')) < 2 or separate_line[0].split('.')[0] == '':
                """ Check the filename and extension"""
                print(f"File name error \n--- {line} ---\n in line {num_line}. Check the filename: {separate_line[0]}")
                exit()
            else:
                if not os.path.exists(file):
                    """ Check available file"""
                    print(f'{file} NOT FOUND')
            return True

    def _check_hash(self, obj):
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
        try:
            with open(self.path_input_file, "r") as f:
                for num, line in enumerate(f, 1):
                    if len(line.split()) == 0:
                        continue
                    str_line = line.replace('\n', '')
                    if not self._validation_line_in_file(str_line, num):
                        break
                    else:
                        self._check_hash(str_line)
        except FileNotFoundError:
            print(f"File {self.path_input_file} not found")
        except IOError:
            print(f'File {self.path_input_file} not available')


def check_exists_file(value):
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
