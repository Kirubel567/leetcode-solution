# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level, ans, max_sum = 0,0, -float('inf')
        queue = deque()
        queue.append(root)

        while queue: 
            level+=1
            curr_sum = 0

            for i in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)

            if curr_sum > max_sum: 
                max_sum, ans = curr_sum, level

        return ans
