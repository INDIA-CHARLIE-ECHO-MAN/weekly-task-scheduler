import pytest
from error import InputError
import data as datafile
options = ["Open", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_task(task, list):
    if list not in options:
        raise InputError("Invalid list input")            

    if list == "Open":
        datafile.data[list].append(task)

    else:
        datafile.data[list]["Open"].append(task)

def delete_task(index, list):
    if list not in options:
        raise InputError("Invalid list input")  

    if list == "Open":
        datafile.data[list].pop(index)

    else:
        datafile.data[list]["Open"].pop(index)

def assign_task(index, origin, to):
    if origin == "Open":
        task = datafile.data[origin][index]
    else:
        task = datafile.data[origin]['Open'][index]
    add_task(task, to)
    delete_task(index, origin)


def rearrange_task(task, position):
    pass

def reset():
    datafile.data = {
    "Open": [],
    "Monday": {
        "Open": [],
        "Closed": []
    },
    "Tuesday": {
        "Open": [],
        "Closed": []
    },
    "Wednesday": {
        "Open": [],
        "Closed": []
    },
    "Thursday": {        
        "Open": [],
        "Closed": []
    },
    "Friday": {        
        "Open": [],
        "Closed": []
    },
    "Saturday": {       
        "Open": [],
        "Closed": []
    },
    "Sunday": {        
        "Open": [],
        "Closed": []
    }
}