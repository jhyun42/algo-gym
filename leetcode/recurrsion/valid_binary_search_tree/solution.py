# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def is_valid_bst(root):
    def validate(node, low=-float('inf'), high=float('inf')):

        if node is None:
            return True

        if node.val <= low or node.val >= high:
            return False

        return (validate(node.right, node.val, high) and
                validate(node.left, low, node.val))

    return validate(root)
