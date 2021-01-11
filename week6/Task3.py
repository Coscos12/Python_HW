def html_decorator(tag, N):
    def decorator(func):

        def wrapper(text):
            s = []
            result = func(text)
            for i in range(N):
                s.append(f'<{tag}>{result.capitalize()} {i+1}</{tag}>')
            return s
        return wrapper
    return decorator


@html_decorator("li", 3)
def html_element(text):
    new_text = text
    to_replace =['@', '#', '%', '&', '$', '^', '*', '_']
    to_delete = ['<', '>', '/']
    for i in new_text:
        if i in to_replace:
            new_text = new_text.replace(i, " ")
        elif i in to_delete:
            new_text = new_text.replace(i, "")
    return new_text
