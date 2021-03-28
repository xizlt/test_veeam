import pytest

from test2 import CheckHash


@pytest.mark.parametrize('line', [('file_02.txt sha1 fefb677369d7894997575b0e448c40e3'),
                                  ('78.file_02.txt sha1 fefb677369d7894997575b0e448c40e3'), ])
def test_name_file_good(line):
    num_line = 10
    name = line.split(' ')[0]
    f = CheckHash('data.txt', '').check_name_file(line, num_line, name)
    assert f == True


@pytest.mark.parametrize('line', [('file_02 sha1 fefb677369d7894997575b0e448c40e3'),
                                  ('.txt sha1 fefb677369d7894997575b0e448c40e3'), ])
def test_name_file_bad(capfd, line):
    num_line = 10
    name = line.split(' ')[0]
    f = CheckHash('data.txt', '').check_name_file(line, num_line, name)
    captured, err = capfd.readouterr()

    assert f == False
    assert captured == f"File name error \n--- {line} ---\n in line {num_line}. Check the filename: {name}\n"
