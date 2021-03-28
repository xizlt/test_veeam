import pytest

from test2 import CheckHash


def test_good():
    path = 'files/file_03.txt'
    assert CheckHash('files/data.txt', '').check_path_file(path) == True


@pytest.fixture()
def test_path_bad(capfd):
    path = 'file_03.txt'
    f = CheckHash('data.txt', '').check_path_file(path)
    captured, err = capfd.readouterr()

    assert f == False
    assert captured == f'{path} NOT FOUND\n'
