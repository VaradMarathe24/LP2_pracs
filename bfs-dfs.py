from collections import deque

# Node structure for a binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

# Recursive DFS - Preorder Traversal (Root → Left → Right)
def dfs_recursive(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)           # Visit the node
        dfs_recursive(root.left, result)  # Go left
        dfs_recursive(root.right, result) # Go right
    return result

# Iterative BFS - Level Order Traversal
def bfs_iterative(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)           # Visit the node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Execution
print("DFS (Preorder Recursive):", dfs_recursive(root))
print("BFS (Level Order Iterative):", bfs_iterative(root))
