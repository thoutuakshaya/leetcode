# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans=0
        def yes(node,previousdirection,s):
            nonlocal ans
            if node is None:
                return
            ans=max(ans,s)
            if previousdirection=='right':
                yes(node.left,'left',s+1)
                yes(node.right,'right',1)
            else:
                yes(node.right,'right',s+1)
                yes(node.left,'left',1)
        yes(root,"left",0)
        yes(root,"right",0)
        return ans