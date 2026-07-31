# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def ro(rootu,maxi):
            if rootu is None:
                return 0
            if rootu.val >=maxi and root is not None:
                c=1
            else :
                c=0
                
            maxi=max(rootu.val,maxi)
            return c+ro(rootu.left,maxi)+ro(rootu.right,maxi)
        
        return ro(root,root.val)
        