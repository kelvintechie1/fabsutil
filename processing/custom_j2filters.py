from re import search

def regexFilter(value, regex):
    if search(rf"{regex}", value) is not None:
        return True
    return False