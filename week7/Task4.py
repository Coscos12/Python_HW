def circle_iterator(lst, end):
    counter = 0
    divider = len(lst)
    while counter < end:
        yield lst[counter % divider]
        counter += 1
