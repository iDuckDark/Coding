class Student(object):
    def __init__(self, name="none"):
        self.name = name

    def __repr__(self):
        return self.name


def foo1():
    return "foo1"


def foo2():
    return "foo2"


def foo3():
    return "foo3"


def main():
    # Classes
    hashmap = {}
    for i in range(5):
        hashmap[i] = Student
    print(hashmap)
    print(hashmap[0] is hashmap[1])
    # Functions
    functions = [foo1, foo2, foo3]
    print(functions[0])

# main()

string = f'string 123'
print(string)
