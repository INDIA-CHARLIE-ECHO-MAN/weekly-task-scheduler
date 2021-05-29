"""Tests assign_task function

"""
from error import InputError
import pytest 
from thandle import add_task
from thandle import delete_task
from thandle import assign_task
from thandle import reset
import data as datafile

@pytest.fixture(autouse = True)
def restart():
    """Resets data before each test

    Does not return anything.
    """
    reset()

"""
Following tests below checks if tasks allocated to one list can be assigned to another list.

Assumptions:
    - App won't be able to assign a task from current to list to itself
"""

panels_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def assign_task_days(day):
    for panel in panels_list:
        if panel is not day:
            task = "do this"
            index = 0
            add_task(task, day)
            if day == "Open":
                access = datafile.data["Open"]
            else:
                access = datafile.data[day]["Open"]
            assign_task(index, day, panel)
            assert len(access) == 0
            assert len(datafile.data[panel]["Open"]) == 1
            

def test_assign_task_days():
    for day in panels_list:
        assign_task_days(day)
        reset()

"""
Tests if InputError occurs when invalid list is inputted
"""

def test_assign_task_bad_list():
    task = "do this"
    day = "Monday"
    add_task(task, day)
    with pytest.raises(InputError):
        assign_task(0, day, "Your mum")
