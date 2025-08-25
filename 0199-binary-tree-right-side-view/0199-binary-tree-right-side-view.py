# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        ans = []

        if root: 
            queue.append(root)

        while len(queue) > 0: 
            arr = []
            for _ in range(len(queue)): 
                curr = queue.popleft()
                arr.append(curr)
                if curr.right: 
                    queue.append(curr.right)
                if curr.left: 
                    queue.append(curr.left)
            
            #search for a number from arr
            for i in range(len(arr)): 
                if arr[i]: 
                    ans.append(arr[i].val)
                    break
        
        return ans
                