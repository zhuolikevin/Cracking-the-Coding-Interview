class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

from collections import deque

def hasPath(start, end):
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if neighbor == end:
                    return True
                else:
                    queue.append(neighbor)
    return False

# Test
A = GraphNode('A')
B = GraphNode('B')
C = GraphNode('C')
D = GraphNode('D')
E = GraphNode('E')
F = GraphNode('F')
G = GraphNode('G')
A.neighbors = [B, E]
B.neighbors = [A, C]
C.neighbors = [D, F]
D.neighbors = [B]
E.neighbors = [F]
F.neighbors = []
G.neighbors = [B]

print hasPath(A, F)
print hasPath(A, G)
