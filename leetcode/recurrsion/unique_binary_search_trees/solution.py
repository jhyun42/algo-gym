# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_trees(n):
    def helper(start, end):

        if start > end:
            return [None, ]

        all_trees = []

        # Pick up a root
        for idx in range(start, end + 1):

            # All possible left sub-trees if idx is choosen to be a root
            left_trees = helper(start, idx - 1)

            # All possible right sub-trees if idx is choosen to be a root
            right_trees = helper(idx + 1, end)

            for l in left_trees:
                for r in right_trees:
                    curr_tree = TreeNode(idx)
                    curr_tree.left = l
                    curr_tree.right = r
                    all_trees.append(curr_tree)

        return all_trees

    return helper(1, n) if n else []
