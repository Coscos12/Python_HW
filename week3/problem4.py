def is_palindrome(x):
    new_list = []
    for i in x:
        k = i[::-1]
        if k == i:
            new_list.append(i)
    return new_list
