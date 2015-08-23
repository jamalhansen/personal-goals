from os import getcwd
from os.path import join, isfile

import pytest


from pg_tools.weekly_update import WeeklyUpdate

@pytest.fixture
def source_dir():
    current_dir = getcwd()
    return join(current_dir, 'tests', 'fixtures')

@pytest.fixture
def basic_list():
    return "basic_list.md"

def source_file_contents(source_dir, file_name):
    """ returns the contents of a file """
    file_n_path = join(source_dir, file_name)
    with open(file_n_path, encoding='utf-8') as checked:
        return checked.read().rstrip()

@pytest.fixture
def basic_list_dco(source_dir):
    """ returns the desired checked output for basic list """
    return source_file_contents(source_dir, "basic_list_dco.md")

@pytest.fixture
def basic_list_duo(source_dir):
    """ returns the desired unchecked output for basic list """
    return source_file_contents(source_dir, "basic_list_duo.md")

@pytest.fixture
def target_checked_local(tmpdir):
    return tmpdir.join("target_checked.md")

@pytest.fixture
def target_unchecked_local(tmpdir):
    return tmpdir.join("target_unchecked.md")

@pytest.fixture
def wu(source_dir, basic_list, target_checked_local, target_unchecked_local):
    return WeeklyUpdate(source_dir, basic_list,
                        target_checked_local, target_unchecked_local)
