def first_last(a):
    if len(a) < 2:
        return ''
    return a[0:2]+a[-2:]
