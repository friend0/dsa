import collections
from typing import List, Optional

from binary_tree.tree_node import TreeNode


class Solution:

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        columns = {}
        queue = collections.dequeue([0, root])

        res = []
        col_min, col_max = 0, 0
        while queue:
            col, node = queue.popleft()

            if val := columns.get(col) is None:
                val[col] = []
            columns[col].append(node.val)

            col_min = min(col, col_min)
            col_max = max(col, col_max)

            if node.left:
                queue.append((col - 1, node.left))
            if node.right:
                queue.append((col + 1), node.right)

        for row in range(col_min, col_max + 1):
            res.append(columns.get[row])
        return res
