class TreeNode:

    def __init__(self,
                 val=0,
                 l: 'TreeNode' = None,
                 r: 'TreeNode' = None) -> None:
        self.val = val
        self.left = l
        self.right = r
