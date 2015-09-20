from os.path import join
from os import getcwd
from py import path

import pytest
import py

from pg_tools.weekly_update import WeeklyUpdate


def test_charlie_uses_quick_shortcut(tmpdir):
    # Charlie wants an eaiser way that makes some assumptions.
    goals = new Goals(source_dir, temp_dir

    current_dir = getcwd()
    source_dir = join(current_dir, 'tests', 'fixtures')
    source = "basic_list.md"
    checked_out = tmpdir.join("target_checked.md")
    unchecked_out = tmpdir.join("target_unchecked.md")

    assert isinstance(checked_out, py.path.local)

    wu = WeeklyUpdate(source_dir, source, checked_out, unchecked_out)

    # now he check his output
    assert not wu.checked_target.check(exists=1)
    assert not wu.unchecked_target.check(exists=1)
    wu.wrap_up_week()

    # and checks for the new file
    assert wu.checked_target.check(exists=1)
    assert wu.unchecked_target.check(exists=1)

    # and that it contains 3 lines
    text = wu.checked_target.read()

    lines = text.split("\n")
    assert len(lines) == 3

    # and that the lines contain the correct text
    for line in lines:
        assert line[:5].upper() == "- [X]"
        assert line[6:].upper().strip() == "CHECKED"

    # and that the checked items are removed from the original file
    text = wu.unchecked_target.read()

    assert "Checked" not in text

    # Satisfied she starts writing her blog post about her week
