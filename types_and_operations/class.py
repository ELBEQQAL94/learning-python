# define class
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def firstname(self):
        return self.firstname
    def lastname(self):
        return self.lastname
    def fullname(self):
        return self.firstname + self.lastname

person = Person('youssef', 'elbeqqal', 25)

print(person.firstname())

# TypeError: 'str' object is not callable