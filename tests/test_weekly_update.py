from os import getcwd
from os.path import join, isfile

import pytest

from helpers import *
from pg_tools.weekly_update import *


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

def test_valid_line():
    assert valid_line("     ")
    assert valid_line("- [X]")
    assert valid_line("ssssssssss\n")
    assert valid_line("dkff;lk;lsdkf")

def test_is_not_valid_line():
    assert not valid_line("1234")
    assert not valid_line("")
    assert not valid_line("\n")
    assert not valid_line("")

def test_is_whitespace():
    assert is_whitespace("\n")
    assert is_whitespace(" ")
    assert is_whitespace("   \t\n")

def test_is_not_whitepspace():
    assert not is_whitespace("sdfkljflsj")
    assert not is_whitespace("1")
    assert not is_whitespace("2\n")

def test_checked_line():
    assert checked_line("- [x]pdek eopd we pwekpewk")
    assert checked_line("- [X]EW)ECMLD:MC DS")

def test_not_checked_line():
    assert not checked_line("      ")
    assert not checked_line("dklsdds fpdsf d")
    assert not checked_line("d- [x]d;;ds")
