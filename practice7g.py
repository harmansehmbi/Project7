class User:
    pass
class Driver:
    pass

data = []
print(type(data))

# 1. Object Construction Statement

u = User()
v = User()
d = Driver()

print(u, type(u))
print(d, (type(d)))
print(v,type(v))

# 2. Write Data in Object

u.name = "John"
u.phone = "9872111045"
u.email = "john@example.com"
u.address = "Redwood Shores"

v.name = "Fionna"
v.age = 90
v.salary = 30000

d.name = "George"
d.phone = "98754357889"
d.experience = 9
d.licesnce = "PBXS567"