import pytest

from test2 import CheckHash


def test_path_main_file_open():
    path = 'files/data.txt'
    CheckHash(path, '').read_file()


@pytest.mark.parametrize('path', [('gfhfg/gh.txt'),
                                  ('no.txt'),
                                  (' ')])
def test_path_main_file_raises_not_found(capfd, path):
    with pytest.raises(FileNotFoundError):
        CheckHash(path, '').read_file()
        captured, err = capfd.readouterr()
        assert captured == f"File {path} not found\n"


def test_path_main_file_empty(capfd):
    path = 'files/empty.txt'
    with pytest.raises(SystemExit):
        CheckHash(path, '').read_file()
        captured, err = capfd.readouterr()
        assert captured == f"File {path} empty\n"
