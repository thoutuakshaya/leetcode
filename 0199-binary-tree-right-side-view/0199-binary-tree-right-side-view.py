# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        s=[]
        def right(node,level):
            if node is None:
                return
            if level==len(s):
                s.append(node.val)
            else:
                s[level]=node.val
            right(node.left,level+1)
            right(node.right,level+1)
        right(root,0)
        return s