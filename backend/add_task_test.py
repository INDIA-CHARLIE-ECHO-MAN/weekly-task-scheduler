"""Tests add_task function

"""
from error import InputError
import pytest 
from thandle import add_task
from thandle import reset
import data as datafile

@pytest.fixture(autouse = True)
def restart():
    """Resets data before each test

    Does not return anything.
    """
    reset()


"""
Following tests below checks if multiple tasks can added in a queue like fashion.
"""

def test_add_task_Monday():
    task = "do this"
    day = "Monday"
    add_task(task, day)
    access = datafile.data['Monday']['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"

def test_add_task_Tuesday():
    task = "do this"
    day = "Tuesday"
    add_task(task, day)
    access = datafile.data['Tuesday']['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"

def test_add_task_Wednesday():
    task = "do this"
    day = "Wednesday"
    add_task(task, day)
    access = datafile.data['Wednesday']['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"

def test_add_task_Thursday():
    task = "do this"
    day = "Thursday"
    add_task(task, day)
    access = datafile.data['Thursday']['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"

def test_add_task_Friday():
    task = "do this"
    day = "Friday"
    add_task(task, day)
    access = datafile.data['Friday']['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"

def test_add_task_Saturday():
    task = "do this"
    day = "Saturday"
    add_task(task, day)
    access = datafile.data['Saturday']['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"

def test_add_task_Sunday():
    task = "do this"
    day = "Sunday"
    add_task(task, day)
    access = datafile.data['Sunday']['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"
    
def test_add_task_open():
    task = "do this"
    day = "Open"
    add_task(task, day)
    access = datafile.data['Open']
    assert len(access) == 1
    access[0] == "do this"
    add_task(task, day)
    assert len(access) == 2
    access[1] == "do this"

"""
Tests if InputError occurs when invalid list is inputted
"""

def test_add_task_bad_list():
    task = "do this"
    day = "Your mum"
    with pytest.raises(InputError):
        add_task(task, day)
