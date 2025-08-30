"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: 
            return []

        stack = [root]
        res = []

        while stack: 
            temp = stack.pop()
            res.append(temp.val)
            stack.extend(temp.children[::-1])
        
        return res