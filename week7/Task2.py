def sentense(text):
    lst = text.split()
    counter = 0
    while counter < len(lst):
        yield lst[counter]
        counter += 1


c = (counter for counter in text.split())
