_singleton = None

class Example:
    def __new__(cls):
        global _singleton

        if _singleton is None:
            print("Singleton is None")
            _singleton = super(Example, cls).__new__(cls)

        return _singleton

a = Example()
b = Example()
print(a is b)
print(a == b)
# output: True in Python3