from binary_tree.tree_node import TreeNode


def preorder(r: TreeNode) -> list[int]:
    if r is None:
        return []
    results = [r.val]
    results += preorder(r.left)
    results += preorder(r.right)
    return results


def inorder(r: TreeNode) -> list[int]:
    results = []
    if r is None:
        return results
    results += inorder(r.left)
    results.append(r.val)
    results += inorder(r.right)
    return results
