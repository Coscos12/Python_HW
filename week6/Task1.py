def counter(func):

    func.__count__ = 0

    def wrapper(*args, **kwargs):
        func.__count__ += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} was called: {func.__count__} times')
        return result
    return wrapper
