_singleton = None

class Example:
    def __new__(cls):
        global _singleton

        if _singleton is None:
            _singleton = super(Example, cls).__new__(cls)

        return _singleton

a = Example()
b = Example()
a is b
# output: True