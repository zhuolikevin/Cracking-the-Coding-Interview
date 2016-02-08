class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head):
    # Reverse the first half of the list, O(n) time O(1) space
    if not head or not head.next:
        return True
    slow = head
    fast = head.next
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
    right = slow.next
    slow.next = prev
    left = slow.next if not fast else slow
    while left and right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
