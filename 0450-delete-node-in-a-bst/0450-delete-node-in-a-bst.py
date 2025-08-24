# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, key=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #amma use the right side of the node to replace is so I have to find the min of the right subtree 
        def minValueNode(root): 
            curr = root
            while curr and curr.left: 
                curr = curr.left

            return curr

        #first find the deleted node from the BST
        if not root: 
            return None
        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)
        #then delete it if you find the deleted node using the following else
        else:
            #first check for case one in which the deleted node has one or two children
            if not root.left: 
                return root.right #return the right if left is null(make the right the new replacement)
            elif not root.right: 
                return root.left #if right is null make the left the new replacement 
            #now continue to case two in which is has two children, choose the right subtree then find the min node using minValueNode() then replace it with root
            else: 
                minNode = minValueNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
            

        

