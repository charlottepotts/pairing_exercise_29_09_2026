from lib.see_participants import *

def test_with_one_name():
    participant = see_participants(["Charlotte"])
    assert participant == "Charlotte"

def test_with_two_names():
     participant = see_participants(["Charlotte" , "Atisha"])
     assert participant == "Charlotte & Atisha"

def test_with_three_names():
     participant = see_participants(["Charlotte" , "Atisha" , "Ben"])
     assert participant == "Charlotte, Atisha & Ben"
