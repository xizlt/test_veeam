import pytest

from test2 import CheckHash


def test_line_good():
    line = 'file_03.txt md5 fefb677369d7894997575b0e448c40e3'
    assert CheckHash('data.txt', '').validation_line_in_file(line, 1) == True


def test_line_columns_more():
    line = 'file_02.txt md5 fefb677369d7894997575b0e448c40e3 four-column'
    assert CheckHash('data.txt', '').validation_line_in_file(line, 1) == False
    assert CheckHash('data.txt', '').validation_line_in_file(line, 1) == "Invalid string "
                                                                         "--- file_02.txt md5 fefb677369d7894997575b0e448c40e3 four-column ---"
                                                                         " in line 1. Count columns must be: 3}"


def test_line_columns_less():
    line = 'file_02.txt md5'
    assert CheckHash('data.txt', '').validation_line_in_file(line, 1) == False
