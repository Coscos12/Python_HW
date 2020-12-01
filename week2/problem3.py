counter = int(input("input quantity "))
if counter < 1:
    raise Exception("looks like negative number")
for i in range(counter + 1):
    print("*" * i)
