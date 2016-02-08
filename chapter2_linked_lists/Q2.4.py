class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head, pivot):
    # Stable, O(n) time O(1) space
    dummyLeft, dummyRight = ListNode(0), ListNode(0)
    left, right = dummyLeft, dummyRight
    curNode = head
    while curNode:
        if curNode.val < pivot:
            left.next = curNode
            left = left.next
        else:
            right.next = curNode
            right = right.next
        curNode = curNode.next
    left.next = dummyRight.next
    right.next = None
    return dummyLeft.next

# Test
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(1)
E = ListNode(4)
F = ListNode(4)
G = ListNode(5)
H = ListNode(1)
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H

newHead = partition(A, 2)
while newHead:
    print str(newHead.val) + '->',
    newHead = newHead.next
