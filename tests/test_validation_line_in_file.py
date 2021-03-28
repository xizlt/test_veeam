import pytest

from test2 import CheckHash


@pytest.mark.parametrize('line', [('file_02.txt sha1 fefb677369d7894997575b0e448c40e3')])
def test_good(line):
    id_line = 5
    separate_line = line.split(' ')
    assert CheckHash('data.txt', '').validation_line_in_file(line, id_line, separate_line) == True


@pytest.mark.parametrize('line', [('file_02.txt sha1 fefb677369d7894997575b0e448c40e3 four-column'),
                                  ('file_02.txt sha1'),
                                  ('file_02.txt fefb677369d7894997575b0e448c40e3'),
                                  ('  file_02.txt fefb677369d7894997575b0e448c40e3'),
                                  ('file_02.txt fefb677369d7894997575b0e448c40e3  '),
                                  ('  file_02.txt       fefb677369d7894997575b0e448c40e3    '), ])
def test_columns_bad(capfd, line):
    columns_in_row = 3
    id_line = 10
    separate_line = line.split(' ')
    f = CheckHash('data.txt', '').validation_line_in_file(line, id_line, separate_line)
    captured, err = capfd.readouterr()

    assert f == False
    assert captured == f"Invalid string \n--- {line} ---\nin line {id_line}. Count columns must be: {columns_in_row}\n"


def test_empty_line():
    path = 'files/data.txt'
    assert CheckHash(path, '').read_file() == None
