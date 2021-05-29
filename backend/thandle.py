import pytest
from error import InputError
import data as datafile
options = ["Open", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def input_error(panel):
    if panel not in options:
        raise InputError("Invalid panel input")    

def add_task(task, panel):
    input_error(panel)          

    if panel == "Open":
        datafile.data[panel].append(task)

    else:
        datafile.data[panel]["Open"].append(task)

def delete_task(index, panel):
    input_error(panel)

    if panel == "Open":
        datafile.data[panel].pop(index)

    else:
        datafile.data[panel]["Open"].pop(index)

def assign_task(index, panel, to):
    if panel == "Open":
        task = datafile.data[panel][index]
    else:
        task = datafile.data[panel]['Open'][index]
    add_task(task, to)
    delete_task(index, panel)


def rearrange_task(init_pos, fin_pos, panel):
    input_error(panel)

    if panel == "Open":
        access = datafile.data[panel]
    
    else:
        access = datafile.data[panel]["Open"]

    old = access[init_pos]
    access[init_pos] = access[fin_pos]
    access[fin_pos] = old
    

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