def num_and_apl(string):
    return [i for i in string.split(' ') if(i.isalnum() is True and i.isalpha() is False and i.isdigit() is False)]
