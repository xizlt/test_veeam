from test2 import CheckHash


def test_path_input_folder():
    path = 'folder'
    assert CheckHash(path, '').create_path(path) == 'folder/'


def test_path_input_name_file():
    path = 'no.txt'
    assert CheckHash(path, '').create_path(path) == 'no.txt'


def test_path_input_folder_slash():
    path = 'folder/'
    assert CheckHash(path, '').create_path(path) == 'folder/'


def test_path_input_file_slash():
    path = 'folder/no.txt'
    assert CheckHash(path, '').create_path(path) == 'folder/no.txt'


def test_path_input_empty():
    path = '/'
    assert CheckHash(path, '').create_path(path) == '/'
