class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def genBST(inputList):
    if not inputList: return None
    middle = len(inputList) / 2
    root = TreeNode(inputList[middle])
    root.left = genBST(inputList[:middle])
    root.right = genBST(inputList[middle+1:])
    return root
