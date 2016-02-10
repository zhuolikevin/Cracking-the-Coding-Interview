class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self, value):
        self.inStack.append(value)

    def dequeue(self):
        if self.outStack:
            return self.outStack.pop()
        self.moveStack()
        if self.outStack:
            return self.outStack.pop()
        else:
            raise IndexError('The queue is empty!')

    def peek(self):
        self.moveStack()
        if self.outStack:
            return self.outStack[0]
        else:
            raise IndexError('The queue is empty!')

    def moveStack(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())

# Test
myQ = MyQueue()
myQ.enqueue('A')
print myQ.inStack, myQ.outStack
myQ.enqueue('B')
print myQ.inStack, myQ.outStack
myQ.enqueue('C')
print myQ.inStack, myQ.outStack
print 'dequeue: ', myQ.dequeue()
print myQ.inStack, myQ.outStack
myQ.enqueue('D')
print myQ.inStack, myQ.outStack
myQ.enqueue('E')
print myQ.inStack, myQ.outStack
print 'dequeue: ', myQ.dequeue()
print myQ.inStack, myQ.outStack
print 'dequeue: ', myQ.dequeue()
print myQ.inStack, myQ.outStack
print 'dequeue: ', myQ.dequeue()
print myQ.inStack, myQ.outStack
