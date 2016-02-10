def sortStack(unsortedStack):
    # O(n^2) time O(n) space
    sortedStack = []
    while unsortedStack:
        cur = unsortedStack.pop()
        while sortedStack and sortedStack[-1] > cur:
            unsortedStack.append(sortedStack.pop())
        sortedStack.append(cur)
    return sortedStack

stack = [5,7,10,12,3,6]
print sortStack(stack)
