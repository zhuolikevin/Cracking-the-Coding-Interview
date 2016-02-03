class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    if not node: return
    if not node.next:
        node = None
        return

    node.val = node.next.val
    node.next = node.next.next

# Test
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)
F = ListNode(6)
G = ListNode(7)
H = ListNode(8)
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H

# node not at the end/head
deleteNode(D)
node = A
while node:
    print node.val
    node = node.next

# head node
deleteNode(A)
node = B
while node:
    print node.val
    node = node.next

# end node (cannot handle)
deleteNode(H)
node = A
while node:
    print node.val
    node = node.next
