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