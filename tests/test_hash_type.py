import pytest

from test2 import CheckHash


@pytest.mark.parametrize('line', [('file_02.txt sha1 fefb677369d7894997575b0e448c40e3'),
                                  ('file_02.txt MD5 fefb677369d7894997575b0e448c40e3')])
def test_hash_type_good(capfd, line):
    num_line = 10
    type = line.split(' ')[1].lower()
    f = CheckHash('data.txt', '').check_hash_type(line, num_line, type)
    assert f == True


@pytest.mark.parametrize('line', [('file_02.txt sha fefb677369d7894997575b0e448c40e3'),
                                  ('file_02.txt tst fefb677369d7894997575b0e448c40e3')])
def test_hash_type_bad(capfd, line):
    num_line = 10
    hash_type = ['md5', 'sha1', 'sha256', 'test']
    type = line.split(' ')[1].lower()
    f = CheckHash('data.txt', '').check_hash_type(line, num_line, type)
    captured, err = capfd.readouterr()
    assert f == False
    assert captured == f"\nInvalid encoding method: {type}\n--- {line} ---\nin line {num_line}. Available encoding: {hash_type}\n"


@pytest.mark.parametrize('line', [('file_02.txt test fefb677369d7894997575b0e448c40e3')])
def test_hash_type_not_support(capfd, line):
    num_line = 10
    type = line.split(' ')[1].lower()
    f = CheckHash('data.txt', '').check_hash_type(line, num_line, type)
    captured, err = capfd.readouterr()
    assert f == False
    assert captured == 'This type "test" is not supported\n'