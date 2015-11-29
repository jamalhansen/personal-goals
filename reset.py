#! /usr/bin/env python3

from os import getcwd
from py import path

import py

from pg_tools.weekly_update import WeeklyUpdate
from pg_tools.goals import Goals


# Charlie wants an eaiser way that makes some assumptions.
current_dir = getcwd()

source = "README.md"
local = py.path.local(current_dir)

checked_out = local.join("README.md.checked")
unchecked_out = local.join("README.md.new")

wu = WeeklyUpdate(current_dir, source, checked_out, unchecked_out)
wu.wrap_up_week()
