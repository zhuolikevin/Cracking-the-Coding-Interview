class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates1(head):
    # O(n) time O(n) space
    if not head: return None

    existed = set()
    node, prev = head, ListNode(0)
    while node:
        if node.val in existed:
            prev.next = node.next
        else:
            existed.add(node.val)
            prev = node
        node = node.next

def deleteDuplicates2(head):
    # O(n^2) time O(1) space
    if not head: return None

    node = head
    while node:
        check = node
        while check.next:
            if check.next.val == node.val:
                check.next = check.next.next
            else:
                check = check.next
        node = node.next

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

print 'Solution1:'
print 'Before'
node = A
while node:
    print node.val
    node = node.next
print 'After'
deleteDuplicates1(A)
node = A
while node:
    print node.val
    node = node.next


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

print 'Solution2:'
print 'Before'
node = A
while node:
    print node.val
    node = node.next
print 'After'
deleteDuplicates2(A)
node = A
while node:
    print node.val
    node = node.next
