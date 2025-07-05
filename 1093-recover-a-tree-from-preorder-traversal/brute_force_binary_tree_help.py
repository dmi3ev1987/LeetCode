from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None

        stack = []  # Stack to keep track of nodes at different depths
        index = 0
        length = len(traversal)

        while index < length:
            # Parse depth
            depth = 0
            while index < length and traversal[index] == '-':
                depth += 1
                index += 1

            # Parse value
            value_string = []
            while index < length and traversal[index].isdigit():
                value_string.append(traversal[index])
                index += 1
            value = int(''.join(value_string))

            # Create new node
            node = TreeNode(value)

            # If depth is 0, it's the root
            if depth == 0:
                stack = [node]
                continue

            # Find parent (last node at depth-1)
            while len(stack) > depth:
                stack.pop()

            # Attach to parent
            parent = stack[-1]
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

            stack.append(node)

        return stack[0] if stack else None


def print_tree(root, level=0, prefix='Root: '):
    if root is not None:
        print(' ' * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            print_tree(root.left, level + 1, 'L--- ')
            print_tree(root.right, level + 1, 'R--- ')


solution = Solution()
traversal = '1-2--3--4-5--6---10----11-----55-----100--7---8---9'
result_tree = solution.recoverFromPreorder(traversal)
print_tree(result_tree)
