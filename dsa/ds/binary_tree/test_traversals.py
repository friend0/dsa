import unittest
from binary_tree.tree_node import TreeNode
from binary_tree.traversals import inorder, preorder


class TestTraversals(unittest.TestCase):

    def test_preorder_traversal(self):
        # Test cases: (input tree, expected preorder traversal)
        test_cases = [
            # Test case 1: Empty tree
            (None, []),

            # Test case 2: Single node tree
            (TreeNode(1), [1]),

            # Test case 3: Tree with only left children
            (TreeNode(1, TreeNode(2, TreeNode(3))), [1, 2, 3]),

            # Test case 4: Tree with only right children
            (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), [1, 2, 3]),

            # Test case 5: Balanced tree
            (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]),

            # Test case 6: Full binary tree
            (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                      TreeNode(3, TreeNode(6),
                               TreeNode(7))), [1, 2, 4, 5, 3, 6, 7]),

            # Test case 7: Complete binary tree
            (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                      TreeNode(3, TreeNode(6))), [1, 2, 4, 5, 3, 6])
        ]

        for i, (tree, expected) in enumerate(test_cases):
            result = preorder(tree)
            assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"

    def test_inorder_traversal(self):
        test_cases = [
            (None, []), (TreeNode(1), [1]),
            (TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))),
             [1, 2, 3, 4, 5]),
            (TreeNode(
                1, None,
                TreeNode(2, None,
                         TreeNode(3, None,
                                  TreeNode(4, None,
                                           TreeNode(5))))), [1, 2, 3, 4, 5]),
            (TreeNode(3, TreeNode(1, None, TreeNode(2)),
                      TreeNode(5, TreeNode(4))), [1, 2, 3, 4, 5]),
            (TreeNode(6, TreeNode(4, TreeNode(2, None, TreeNode(3))),
                      TreeNode(8, TreeNode(7), TreeNode(10, TreeNode(9)))),
             [2, 3, 4, 6, 7, 8, 9, 10]),
            (TreeNode(
                7,
                TreeNode(3, TreeNode(1), TreeNode(5, TreeNode(4),
                                                  TreeNode(6))),
                TreeNode(8, None, TreeNode(10))), [1, 3, 4, 5, 6, 7, 8, 10])
        ]

        for i, (tree, expected) in enumerate(test_cases):
            result = inorder(tree)
            assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print("All test cases passed!")
