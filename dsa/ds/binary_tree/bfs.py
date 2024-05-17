import collections
from typing import Optional

from binary_tree.tree_node import TreeNode


def bfs(root: Optional[TreeNode]):
    results = []
    if not root:
        return []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        results.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return results


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

res = bfs(tree)
print(res)
