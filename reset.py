#! /usr/bin/env python3

from os import getcwd
from py import path
from datetime import date


import py

from pg_tools.weekly_update import WeeklyUpdate
from pg_tools.goals import Goals


# Charlie wants an eaiser way that makes some assumptions.
current_dir = getcwd()

source = "README.md"
local = py.path.local(current_dir)

checked_out = local.join("README.md.checked")
unchecked_out = local.join("README.md.new")

day = date.today()
accom_file = day.strftime("%Y-%m-%d")
accom_file = "{0}.md".format(accom_file)
accom_out = local.join("accomplishments", accom_file)

wu = WeeklyUpdate(current_dir, source, accom_out, unchecked_out)
wu.wrap_up_week()

# Now let's move stuff to where it goes
unchecked_out.move(local.join(source))
