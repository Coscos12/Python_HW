def list_sum(x):
    total = 0
    for i in x:
        if (type(i) == type([])):
            total = total + list_sum(i)
        else:
            total = total + i
    return total

