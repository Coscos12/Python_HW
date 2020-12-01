cards = {'2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 0, '8': 0, '9': 0, '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
print('try to input cards with coma separator')
user_input = (input().split(", "))
result = 0

for i in user_input:
    try:
       result += cards[i]
    except KeyError:
        raise ValueError('There are not such cards')
print("total result = ", result)
