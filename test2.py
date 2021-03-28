import hashlib
import os
from pathlib import Path

COLUMNS_IN_ROW = 3
HASH_TYPE = ['md5', 'sha1', 'sha256', 'test']
READ_FILE_TYPE = ['txt']


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

    def validation_line_in_file(self, line, id_line, separate_line):
        """
        Check the allowed number of columns in a row
        :param line:
        :param id_line:
        :param separate_line:
        :return:
        """
        if len(separate_line) != COLUMNS_IN_ROW:
            print(f"Invalid string \n--- {line} ---\nin line {id_line}. Count columns must be: {COLUMNS_IN_ROW}")
            return False
        return True

    def check_hash_type(self, line, id_line, hash_name):
        """
        Check hash type in the available list
        :param line:
        :param id_line:
        :param hash_name:
        :return:
        """
        if hash_name not in HASH_TYPE:
            """ Check if the hash name is in the available list """
            print(
                f"\nInvalid encoding method: {hash_name.lower()}\n--- {line} ---\nin line {id_line}"
                f". Available encoding: {HASH_TYPE}")
            return False
        elif hash_name not in (HASH_TYPE and hashlib.algorithms_available):
            """ Check the type hash"""
            print(f'This type "{hash_name}" is not supported')
            return False
        return True

    def check_name_file(self, line, id_line, name):
        """
        Check name file
        :param line:
        :param id_line:
        :param name:
        :return:
        """
        if len(name.split('.')) < 2 or name.split('.')[0] == '':
            """ Check the filename and extension"""
            print(f"File name error \n--- {line} ---\n in line {id_line}. Check the filename: {name}")
            return False
        return True

    def check_path_file(self, path):
        """
        Check path to file in line
        :param path:
        :return:
        """
        if not os.path.exists(path):
            print(f'{path} NOT FOUND')
            return False
        return True

    def check_hash(self, hash_value, hash_actual, file):
        """
        Check if hash sums match
        :param hash_value:
        :param hash_actual:
        :param file:
        :return:
        """

        if hash_value == hash_actual:
            print(f'{file} OK')
        else:
            print(f'{file} FAIL')

    def read_file(self):
        """
        Opens a file for reading
        :return: None
        """
        try:
            if Path(self.path_input_file).stat().st_size == 0:
                print(f"File {self.path_input_file} empty")
                exit(self.path_input_file)
            if self.path_input_file.split('.')[-1] not in READ_FILE_TYPE:
                print(f'Available file extensions {READ_FILE_TYPE}')
                exit()
            with open(self.path_input_file, "r") as f:
                for num, line in enumerate(f, 1):

                    if len(line.split()) == 0:
                        continue

                    str_line = line.replace('\n', '').strip()
                    separate_line = str_line.split(' ', maxsplit=COLUMNS_IN_ROW)
                    if not self.validation_line_in_file(str_line, num, separate_line):
                        exit()

                    file = self.path_to_files + separate_line[0]
                    hash_name = separate_line[1].lower()
                    hash_value = separate_line[2]
                    hash_actual = hashlib.new(hash_name, file.encode()).hexdigest()

                    if not self.check_hash_type(line, num, hash_name) and \
                            self.check_name_file(line, num, file):
                        exit()
                    elif not self.check_path_file(file):
                        continue
                    else:
                        self.check_hash(hash_value, hash_actual, file)

        except FileNotFoundError:
            print(f"File {self.path_input_file} not found")
            raise

        except IOError:
            print(f'File {self.path_input_file} not available')

        except UnicodeDecodeError:
            print('not support')


def check_exists_file(value):
    """
    Checks the file path.
    :param value: the path to the file
    :return: Bool
    """

    if len(value) == 0 or len(value.split('.')) < 2:
        print('You didn`t specify the file path. Try it again')
        return True
    elif value.split('.')[-1] not in READ_FILE_TYPE:
        print(f'Available file extensions {READ_FILE_TYPE}')
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
