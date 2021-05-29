from thandle import reset
from thandle import add_task
import data as datafile

def test_reset():
    reset()
    origin = {
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
    assert datafile.data == origin
    add_task("to do", "Open")
    reset()
    assert datafile.data == origin


