# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None
        def dfs(node, val): 
            nonlocal ans
            if not node: 
                return 
            elif node.val == val: 
                ans = node
            
            if node.val > val: 
                dfs(node.left, val)
            else: 
                dfs(node.right, val)
        dfs(root, val)
        return ans