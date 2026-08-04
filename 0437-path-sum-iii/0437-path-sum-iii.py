# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
       
        result=0
        def sumpath(node,s):
            nonlocal result
            if node is None:
                return 
            s+=node.val
            if s==targetSum:
                result+=1
            sumpath(node.left,s)
            sumpath(node.right,s)
        def traverse(node):
            if node is None:
                return 
            sumpath(node,0)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return result