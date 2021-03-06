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

def delete_task(index, panel, status):
    input_error(panel)
    status = bool(status)
    if status == True:
        if panel == "Open":
            datafile.data[panel].pop(index)

        else:
            datafile.data[panel]["Open"].pop(index)
    else:
        datafile.data[panel]["Closed"].pop(index)

def assign_task(index, panel, to):
    if panel == "Open":
        task = datafile.data[panel][index]
    else:
        task = datafile.data[panel]['Open'][index]
    add_task(task, to)
    delete_task(index, panel, True)


def rearrange_task(init_pos, fin_pos, panel):
    input_error(panel)

    if panel == "Open":
        access = datafile.data[panel]
    
    else:
        access = datafile.data[panel]["Open"]

    old = access[init_pos]
    access[init_pos] = access[fin_pos]
    access[fin_pos] = old

def close_task(index, panel):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if panel not in days:
        raise InputError("Invalid panel input")

    access = datafile.data[panel]["Closed"]
    task = datafile.data[panel]["Open"][index]
    delete_task(index, panel, True)
    access.append(task)

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