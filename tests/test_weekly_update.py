from os import getcwd
from os.path import join, isfile

import pytest

from tests.helpers import *
from pg_tools.weekly_update import WeeklyUpdate, strip_tail, split_lines, valid_line, is_whitespace, checked_line


def test_weekly_update_has_a_source_dir_attribute(wu, source_dir):
    assert wu.source_dir == source_dir

def test_weekly_update_has_a_source_file_attribute(wu, basic_list):
    assert wu.source_file == basic_list

def test_weekly_update_has_a_target_checked_attribute(wu, target_checked_local):
    assert wu.checked_target == target_checked_local

def test_weekly_update_has_a_target_unchecked_attribute(wu, target_unchecked_local):
    assert wu.unchecked_target == target_unchecked_local

def test_wrap_up_week_creates_checked_target(wu, target_checked_local):
    wu.wrap_up_week()
    assert target_checked_local.check(exists=1)

def test_wrap_up_week_creates_unchecked_target(wu, target_unchecked_local):
    wu.wrap_up_week()
    assert target_unchecked_local.check(exists=1)

def test_can_read_source_file(wu):
    text = wu.read_source_file()
    assert "- [X]" in text

def test_can_filter_checked_items():
    values = ['- [ ] something',
              '- [x] match',
              '# a header',
              '## another header',
              '-[x] garbage',
              '',
              None,
              '- [X] capital match']


    expected_list = ['- [x] match',
                '- [X] capital match']

    actual_list, remainder = split_lines(values)

    assert len(expected_list) == len(actual_list)

    for expected, actual in zip (expected_list, actual_list):
        assert expected == actual

def test_can_remove_checked_from_original(wu):
    values = ['- [ ] something',
              '- [x] match',
              '# a header',
              '## another header',
              '-[x] garbage',
              '',
              None,
              '- [X] capital match']


    expected_list = ['- [ ] something',
              '# a header',
              '## another header',
              '-[x] garbage']

    checked, actual_list = split_lines(values)

    assert len(expected_list) == len(actual_list)

    for expected, actual in zip (expected_list, actual_list):
        assert expected == actual

def test_checked_file_output(wu, basic_list_dco):
    checked, _ = wu.split_source()

    expected_checked_lines = basic_list_dco.split("\n")

    assert len(expected_checked_lines) == len(checked)

    for index, expected in enumerate(expected_checked_lines):
        assert expected == checked[index]

def test_unchecked_file_output(wu, basic_list_duo):
    _, unchecked = wu.split_source()

    expected_unchecked_lines = basic_list_duo.split("\n")

    assert len(expected_unchecked_lines) == len(unchecked)

    for index, expected in enumerate(expected_unchecked_lines):
        assert expected == unchecked[index]

def test_strip_tail():
    source_list = ['foo', ' ', 'bar', None, '', '   ']
    expected_list = ['foo', ' ', 'bar']

    actual_list = strip_tail(source_list)
    assert len(expected_list) == len(actual_list)
    for expected, actual in zip(expected_list, actual_list):
        assert expected == actual


