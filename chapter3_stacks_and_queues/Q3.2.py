class MinStack(object):
    def __init__(self):
        self.minValStack = []
        self.stack = []

    def push(self, x):
        if not self.minValStack or x <= self.getMin():
            self.minValStack.append(x)

        self.stack.append(x)

    def pop(self):
        value = self.stack.pop()
        if value == self.getMin():
            self.minValStack.pop()
        return value

    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.minValStack[-1]
