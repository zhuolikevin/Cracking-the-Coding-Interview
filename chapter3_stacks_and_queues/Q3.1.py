# Here we only provide the implementation for fixed sized stacks

class ThreeStacks(object):
    def __init__(self, stack_size):
        self.stackSize = 100
        self.stackBuffer = [None] * self.stackSize * 3
        self.stackPointers = [-1, -1, -1]

    def push(self, stackNum, value):
        if self.stackPointers[stackNum] + 1 >= self.stackSize:
            raise IndexError('This stack is full!')
        self.stackPointers[stackNum] += 1
        self.stackBuffer[self.absTopOfStack(stackNum)] = value

    def pop(self, stackNum):
        if self.stackPointers[stackNum] == -1:
            raise IndexError('This stack is empty!')
        value = self.stackBuffer[self.absTopOfStack(stackNum)]
        self.stackBuffer(self.absTopOfStack(stackNum)) = None
        self.stackPointers[stackNum] -= 1
        return value

    def absTopOfStack(self, stackNum):
        return stackNum * self.stackSize + self.stackPointers[stackNum]
