def my_encrypt(path, string):
    new_lst = []
    f = open(path + '/temp.bin', 'wb')
    f.write(bytearray(string, 'utf-8'))
    f.close()
    f = open(path + '/temp.bin', 'r')
    for i in f.read():
        new_lst.append(ord(i))
    f.close()
    return new_lst
