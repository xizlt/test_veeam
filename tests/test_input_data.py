import pytest

from test2 import check_exists_file


def test_good(monkeypatch):
    input_value = 'files/data.txt'
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    c = check_exists_file(input_value)
    i = input('Path to the input file:\n')
    assert c == None
    assert i == 'files/data.txt'


@pytest.mark.parametrize('value', [('.txt'),
                                   ('folder/data.txt')
                                   ])
def test_not_found(capfd, value):
    c = check_exists_file(value)
    captured, err = capfd.readouterr()
    assert c == True
    assert captured == 'File on the given path was not found. Check path\n'


@pytest.mark.parametrize('value', [(' '),
                                   ('folder')
                                   ])
def test_bad(capfd, value):
    c = check_exists_file(value)
    captured, err = capfd.readouterr()
    assert c == True
    assert captured == 'You didn`t specify the file path. Try it again\n'
