class Student(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


def main():
    s1 = Student
    s2 = Student
    s3 = Student
