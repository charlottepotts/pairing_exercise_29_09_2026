from lib.see_participants import *

def test_with_one_name():
    participant = see_participants(["Charlotte"])
    assert participant == "Charlotte"