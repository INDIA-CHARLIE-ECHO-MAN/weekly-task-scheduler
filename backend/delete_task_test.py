"""Tests delete_task function

"""
from thandle import close_task
from error import InputError
import pytest 
from thandle import add_task
from thandle import reset
from thandle import delete_task
import data as datafile

@pytest.fixture(autouse = True)
def restart():
    """Resets data before each test

    Does not return anything.
    """
    reset()

"""
Following tests below checks if the task with the correct index is deleted from the list (day)
"""

def test_delete_task_Monday():
    day = "Monday"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]['Open']
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

def test_delete_task_Tuesday():
    day = "Tuesday"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]['Open']
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

def test_delete_task_Wednesday():
    day = "Wednesday"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]['Open']
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

def test_delete_task_Thursday():
    day = "Thursday"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]['Open']
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

def test_delete_task_Friday():
    day = "Friday"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]['Open']
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

def test_delete_task_Saturday():
    day = "Saturday"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]['Open']
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

def test_delete_task_Sunday():
    day = "Sunday"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]['Open']
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

def test_delete_task_open():
    day = "Open"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    delete_task(1, day)
    access = datafile.data[day]
    assert access == [
        "1",
        "3"
    ]
    delete_task(0, day)
    assert access == [
        "3"
    ]

"""
Following tests below check for InputError if they attempt to delete with an invalid index or an invalid list.
"""

def test_delete_task_bad_list():
    day = "Open"
    add_task("1", day)
    add_task("2", day)
    add_task("3", day)
    with pytest.raises(IndexError):
        delete_task(3, day)

    with pytest.raises(InputError):
        delete_task(1, "Hello")

def test_delete_task_closed():
    task1 = "to do1"
    task2 = "to do2"
    panels_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in panels_list:
        add_task(task1, day)
        add_task(task2, day)
        close_task(1, day)
        close_task(0, day)
        delete_task(0, day, False)
        assert len(datafile.data[day]["Closed"]) == 1
        delete_task(0, day, False)
        assert len(datafile.data[day]["Closed"]) == 0

