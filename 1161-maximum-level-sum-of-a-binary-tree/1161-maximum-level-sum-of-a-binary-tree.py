# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        k={}
        def leveldfs(node,level):
            if node is None:
                return
            if level in k:
                k[level]+=node.val
            else:
                k[level]=node.val
            leveldfs(node.left,level+1)
            leveldfs(node.right,level+1)
        leveldfs(root,1)
        m=max(k.values())
        for i,val in k.items():
            if val==m:
                return i
