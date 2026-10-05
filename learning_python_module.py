# module file for learning python

def divide2(value):
    return value / 2

def swap_ab(input):
    split_letters = list(input) # list can be used to split a string into seperate elements in a list
    output = ""
    for item in split_letters:
        if item == "a":
            output += "b"
        elif item == "b":
            output += "a"
        else:
            output += item
    return(output)

