class User:
    pass
class Driver:
    pass

data = []
print(type(data))

# 1. Object Construction Statement

u = User()
d = Driver()

print(type(u))
print((type(d)))

# 2. Write Data in Object

u.name = "John"
u.phone = "9872111045"
u.email = "john@example.com"
u.address = "Redwood Shores"

d.name = "George"
d.phone = "98754357889"
d.experience = "3"
d.licesnce = "PBXS567"