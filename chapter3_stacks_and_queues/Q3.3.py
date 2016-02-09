class SetOfStacks(object):
    def __init__(self, stackSize):
        self.stacks = []
        self.stackSize = stackSize

    def push(self, value):
        last = self.getLastStack()
        if last and len(last) < self.stackSize:
            last.append(value)
        else:
            self.stacks.append([value])

    def pop(self):
        last = self.getLastStack()
        value = last.pop()
        if len(last) == 0:
            self.stacks.pop()

    def getLastStack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

# Test
myStack = SetOfStacks(2)
myStack.push(1) # [1]
print myStack.stacks
myStack.push(2) # [1,2]
print myStack.stacks
myStack.push(3) # [1,2,3]
print myStack.stacks
myStack.pop()   # [1,2]
print myStack.stacks
myStack.push(4) # [1,2,4]
print myStack.stacks
myStack.pop()   # [1,2]
print myStack.stacks
myStack.pop()   # [1]
print myStack.stacks
