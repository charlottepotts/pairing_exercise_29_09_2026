## 1 problem - user story
```
As a member of a group chat,
I want the chat's participants shown as a single readable line,
so that I can see at a glance who's in the conversation.

Acceptance criteria:

No participants: the line is empty.
[] => ""

One participant: just their name.
["Bart"] => "Bart"

Two participants: joined with an ampersand.
["Bart", "Lisa"] => "Bart & Lisa"

Three or more participants: commas between names, with an ampersand before the last one.
["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"

Order is kept: names appear in the same order they were given.
```
## 2 function signature
```python
# Parameters:
# - List of participants
# Return type:
# - String of names of participants in list
# Side Effects:
# - None (that we know of)
def see_participants():
    pass
```

## 3 examples
```python
# scenario 1
see_participants(["Charlotte"]) # "Charlotte"

# scenario 2
list_of_names = ["Charlotte", "Atisha"]
see_participants(list_of_names) # "Charlotte & Atisha"

# scenario 3
list_of_names = ["Charlotte", "Atisha", "Ben"]
see_participants(list_of_names) # "Charlotte, Atisha & Ben"
```