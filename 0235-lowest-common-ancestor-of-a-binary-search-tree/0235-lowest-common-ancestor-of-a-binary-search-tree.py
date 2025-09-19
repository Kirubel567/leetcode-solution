# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #in this question it's all about finding the spliting node of the two nodes or simply they ain't in the same subtree of the tree, so if they ain't in the same subtree then that means the temporary node is their lca
        temp = root 

        while temp: 
            if temp.val > p.val and temp.val > q.val: 
                temp = temp.left
            elif temp.val < p.val and temp.val < q.val:
                temp = temp.right
            else: 
                return temp