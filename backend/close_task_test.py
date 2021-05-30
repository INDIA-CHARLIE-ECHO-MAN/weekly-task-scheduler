from error import InputError
import pytest 
from thandle import add_task
from thandle import reset
from thandle import close_task
import data as datafile

@pytest.fixture(autouse = True)
def restart():
    """Resets data before each test

    Does not return anything.
    """
    reset()

"""
Following tests below checks if tasks assigned to days can be closed.

"""

panels_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def test_close_task():
    task1 = "to do1"
    task2 = "to do2"
    for day in panels_list:
        add_task(task1, day)
        add_task(task2, day)
        close_task(1, day)
        close_task(0, day)
        access = datafile.data[day]["Closed"]
        assert access[0] == task2
        assert access[1] == task1

def test_close_task_bad_list():
    task = "do this"
    day = "Monday"
    add_task(task, day)
    with pytest.raises(InputError):
        close_task(0, "Your mum")
