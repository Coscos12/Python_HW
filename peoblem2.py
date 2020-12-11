def abracadabra(string):
    new_string = string[::-1].replace(string[0], '_', (string.count(string[0])-1))
    return new_string[::-1]
