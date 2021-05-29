"""Tests rearrange_task function

"""
from error import InputError
import pytest 
from thandle import add_task
from thandle import delete_task
from thandle import reset
from thandle import rearrange_task
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
    - App won't be able to rearrange the task's position to itself.
"""

def rearrange_task_day(day):
    task1 = "do this"
    task2 = "do this1"
    task3 = "do this2"
    add_task(task1, day)
    add_task(task2, day)
    add_task(task3, day)

    rearrange_task(0, 1, day)
    if (day == "Open"):
        access = datafile.data["Open"]
    else:
        access = datafile.data[day]['Open']
    assert access[0] == task2
    assert access[1] == task1

    rearrange_task(0, 2, day)
    assert access[2] == task2
    assert access[0] == task3

def test_rearrange_task_days():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        rearrange_task_day(day)
        reset()

def test_rearrange_task_bad_list():
    task1 = "a"
    task2 = "b"
    add_task(task1, "Monday")
    add_task(task2, "Monday")
    with pytest.raises(InputError):
        rearrange_task(0,1,"Your mum")
