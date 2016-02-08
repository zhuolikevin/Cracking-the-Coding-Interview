class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addLists(head1, head2):
    # Number is stored in reverse order
    if not head1: return head2
    if not head2: return head1

    dummyHead = ListNode(0)
    curNode = dummyHead
    carry = 0
    while head1 or head2:
        tempSum = carry
        if head1:
            tempSum += head1.val
            head1 = head1.next
        if head2:
            tempSum += head2.val
            head2 = head2.next
        curNode.next = ListNode(tempSum % 10)
        carry = tempSum / 10
        curNode = curNode.next
        
    if carry:
        curNode.next = ListNode(1)

    return dummyHead.next
