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
print(v,type(v))
print(d, (type(d)))


# 2. Write Data in Object

u.name = "John"
u.phone = "9872111045"
u.email = "john@example.com"
u.address = "Redwood Shores"

v.name = "Fionna"
v.age = 90
v.salary = 30000

# Reference copy

w = v

print(w)

d.name = "George"
d.phone = "98754357889"
d.experience = 9
d.licence = "PBXS567"

# Update Operation in Objects

v.age = 30  # we can also change this with w   # w.age = 30

# Delete Operation in Objects

del u.phone
del d.licence

# Read Operation on Objects

print(u.__dict__)
print(v.__dict__)
print(d.__dict__)