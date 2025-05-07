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

# Helper function to print the preorder result
def print_preorder(result):
    print(" ".join(map(str, result)))

# Level Order Traversal (BFS)
def bfs_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result

# Helper function to print BFS result
def print_level_order(levels):
    for level in levels:
        print(" ".join(map(str, level)))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


# Perform DFS Preorder Traversal
preorder_result = dfs_recursive(root)
print("DFS Preorder Traversal:")
print_preorder(preorder_result)
# Perform BFS Level Order Traversal
level_order_result = bfs_level_order(root)
print("\nBFS Level Order Traversal:")
print_level_order(level_order_result)
