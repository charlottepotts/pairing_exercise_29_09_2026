def see_participants(list_of_names):
    string_of_names = ""
    if len(list_of_names) == 1:
        return list_of_names[0]
    elif len(list_of_names) == 2:
        return f"{list_of_names[0]} & {list_of_names[1]}"
    else:
        return 
        

    # for name in list_of_names:
    #     string_of_names += name
    # return string_of_names
