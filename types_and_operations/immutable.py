# Immutable objects cannot be changed
name = "youssef"
# name[0] = "z"
name = "z" + name[1:]
print(help(len(name)))
# TypeError: 'str' object does not support item assignment