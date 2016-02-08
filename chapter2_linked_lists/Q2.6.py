class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findLoop(head):
    if not head: return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            detect = head
            while detect != slow:
                detect = detect.next
                slow = slow.next
            return slow
    return None
