# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def subtree(node):
            if node is None:
                return 
            if   node==p or node==q:
                return node
            left=subtree(node.left)
            right=subtree(node.right)
            if left and right:
                return node
            if left:
                return left
            return right
        return subtree(root)
        
        