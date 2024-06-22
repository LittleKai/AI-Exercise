class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

stack = Stack(5)

stack.push (1)
stack.push (2)
print(stack.is_full())

print(stack.top())

print(stack.pop())

print(stack.top())

print(stack.pop())

print(stack.is_empty())
