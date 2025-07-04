# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None

        stack = []
        index = 0
        length = len(traversal)

        while index < length:
            depth = 0
            while index < length and traversal[index] == '-':
                depth += 1
                index += 1

            value_string = []
            while index < length and traversal[index].isdigit():
                value_string.append(traversal[index])
                index += 1
            value = int(''.join(value_string))

            node = TreeNode(value)

            if depth == 0:
                stack = [node]
                continue

            while len(stack) > depth:
                stack.pop()

            parent = stack[-1]
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

            stack.append(node)

        return stack[0] if stack else None
