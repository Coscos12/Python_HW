raw_temp = input()
temp = 0
scale = ''
try:
    if raw_temp[-1] == 'C':
        temp = round((int(raw_temp[:-1]) * 1.8 + 32), 2)
        scale = 'F'
        print(raw_temp, "is", str(temp) + scale)
    elif raw_temp[-1] == 'F':
        temp = round(((int(raw_temp[:-1]) - 32)/1.8), 2)
        scale = 'C'
        print(raw_temp, "is", str(temp) + scale)
    else:
        print('Try enter the correct temperature with scale')
except ValueError:
    raise ValueError("it's not a number in your input")
