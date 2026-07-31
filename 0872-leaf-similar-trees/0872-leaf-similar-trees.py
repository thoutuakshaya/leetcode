# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,listu):
            if node is None:
                return
            if node.left is None and node.right is None:
                listu.append(node.val)
            dfs(node.left,listu)
            dfs(node.right,listu)
        arr1=[]
        arr2=[]
        dfs(root1,arr1)
        dfs(root2,arr2)
        return arr1==arr2