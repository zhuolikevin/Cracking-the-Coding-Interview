class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def isBalance(root):
    return False if getHeight(root) == -1 else True

def getHeight(root):
    if not root: return 0

    leftHeight = getHeight(root.left)
    if leftHeight == -1: return -1

    rightHeight = getHeight(root.right)
    if rightHeight == -1: return -1

    return -1 if abs(leftHeight - rightHeight) > 1 else max(leftHeight, rightHeight) + 1

# Test
A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')

# Case 1
# A.left = B
# A.right = C
# B.left = D
# D.left = E

# Case 2
A.left = B
A.right = C
B.left = D
D.right = E

print isBalance(A)
