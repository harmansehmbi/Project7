num = 10
def show():

    global num

    num = 11
    print(">>1. num is :", num)

show()
print(">>2. num is: ", num)

# global keyword is used when you want to change the value of main