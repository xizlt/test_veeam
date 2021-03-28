import hashlib

from test2 import CheckHash


def test_hash_sum_good(capfd):
    hash_value = 'fefb677369d7894997575b0e448c40e3'
    file = 'files/file_03.txt'
    hash_actual = hashlib.new("md5", file.encode()).hexdigest()
    CheckHash('data.txt', '').check_hash(hash_value, hash_actual, file)
    captured, err = capfd.readouterr()
    assert captured == f'{file} OK\n'


def test_hash_sum_bad(capfd):
    hash_value = 'fefb677369d7894997575b0e448c4045'
    file = 'files/file_03.txt'
    hash_actual = hashlib.new("md5", file.encode()).hexdigest()
    CheckHash('data.txt', '').check_hash(hash_value, hash_actual, file)
    captured, err = capfd.readouterr()
    assert captured == f'{file} FAIL\n'
