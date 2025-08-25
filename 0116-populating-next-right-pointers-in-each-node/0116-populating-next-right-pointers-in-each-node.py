"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()

        if root: 
            queue.append(root)

        while len(queue) > 0: 
            prev = None # this is just a pointer to track our next node
            for i in range(len(queue)): 
                curr = queue.popleft()
                if prev: 
                    prev.next = curr
                prev = curr #promote the pointer to the current node
                if curr.left: #we need to move from left to right here 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
            
            

        return root

