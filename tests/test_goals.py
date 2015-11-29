from os import getcwd
from os.path import join, isfile

import pytest

from helpers import *
from pg_tools.goals import *


def test_goals_accepts_source_and_target_directory():
    goals = Goals("source_dir", "target_dir")
    assert "source_dir" == goals.source_dir
    assert "target_dir" == goals.target_dir
