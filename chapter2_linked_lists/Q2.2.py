class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.result = 0

    def findKthToLast1(self, head, k):
        # O(n) time O(n) space. Recursive
        self.helper(head, k)
        return self.result

    def helper(self, head, k):
        if not head:
            return 0
        count = self.helper(head.next, k) + 1
        if count == k:
            self.result = head
        return count

    def findKthToLast2(self, head, k):
        # O(n) time O(1) space
        if not head: return None
        fast = slow = head
        count = 0
        while count < k:
            fast = fast.next
            count += 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
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

solution = Solution()
node1 = solution.findKthToLast1(A, 3)
node2 = solution.findKthToLast2(A, 3)
print node1.val, node2.val
