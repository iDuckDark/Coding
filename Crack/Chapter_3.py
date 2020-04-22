class Stack():
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        saved = self.stack[self.top]
        self.top -= 1
        return saved

    def push(self, elem):
        if self.is_full():
            raise Exception("Stack is full!")
        self.top += 1
        self.stack[self.top] = elem

    def peek(self):
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.stack) - 1

    def __repr__(self):
        return str(self.stack)


def main():
    stack = Stack(5)
    for i in range(1, 5):
        stack.push(i)
    print(stack)


main()
