# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        output = []

        def dfs(root): 
            if not root: 
                return 
            dfs(root.left)
            output.append(root.val)
            dfs(root.right)

        dfs(root)

        dummy = TreeNode(-1)
        curr = dummy 
        for val in output: 
            curr.right = TreeNode(val)
            curr = curr.right
        
        return dummy.right