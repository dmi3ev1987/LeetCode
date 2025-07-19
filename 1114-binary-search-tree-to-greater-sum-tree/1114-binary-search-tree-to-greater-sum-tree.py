# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree_list = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            tree_list.append(current.val)
            current = current.right

        current = root
        sorted_tree_list = sorted(tree_list)

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            current.val = sum(
                sorted_tree_list[sorted_tree_list.index(current.val) :]
            )
            current = current.right

        return root
