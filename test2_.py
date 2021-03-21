import hashlib
import os

COUNT_SEPARATE_IN_LINE = 3
COLUMNS_IN_ROW = 3
HASH_TYPE = ['md5', 'sha1', 'sha256']
PATH_INSIDE_FILE = ''


def validation_line_in_file(line, num_line, path_to_files):
    separate_line = line.split(' ', maxsplit=COUNT_SEPARATE_IN_LINE)

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
            if not os.path.exists(path_to_files + separate_line[0]):
                """ Check available file"""
                print(f'{separate_line[0]} NOT FOUND')
        return True


def check_hash(obj, path_to_files):
    separate_line = obj.split(' ')
    hash_type = separate_line[1].lower()
    hash_sum_provided = separate_line[2]
    file = path_to_files + separate_line[0]

    if hash_type in (HASH_TYPE and hashlib.algorithms_available):
        hash_sum_received = hashlib.new(hash_type, file.encode()).hexdigest()
        if hash_sum_provided == hash_sum_received:
            print(f'{file} OK')
        elif os.path.exists(file):
            print(f'{file} FAIL')
    else:
        print(f'This type "{hash_type}" is not supported')
        exit()


def read_file(path_input_file, path_to_files=""):
    try:
        with open(path_input_file, "r") as f:
            for num, line in enumerate(f, 1):
                if len(line.split()) == 0:
                    continue
                str_line = line.replace('\n', '')
                if not validation_line_in_file(str_line, num, path_to_files):
                    break
                else:
                    check_hash(str_line, path_to_files)
    except FileNotFoundError:
        print(f"File {path_input_file} not found")
    except IOError:
        print(f'File {path_input_file} not available')


if __name__ == '__main__':
    path_input_file = input('path to the input file\n')
    path_to_files = input('path to the directory containing the files to check\n')

    read_file(path_input_file, path_to_files)