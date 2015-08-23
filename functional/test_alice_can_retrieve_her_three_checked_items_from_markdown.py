from os.path import join

import pytest


from tests.helpers import *
from pg_tools.weekly_update import WeeklyUpdate


def test_alice_can_make_an_update_with_marked_off_items(wu):
    # Alice has a list of checked items that she wants to scrape out
    # of a markdown file and move to it's own file
    # She creates a Weekly Update object
    # then she runs the process
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
