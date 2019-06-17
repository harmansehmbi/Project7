num = 10
def show():

    global num

    num = num % 3
    print(">>1. num is :", num)

show()
print(">>2. num is: ", num)

# global is property of main but can be used by anyone.