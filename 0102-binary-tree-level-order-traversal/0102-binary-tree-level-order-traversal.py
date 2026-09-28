# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        arr=defaultdict(list)
        def bfs(root,level):
            if not root:
                return 
            arr[level].append(root.val)
            bfs(root.left,level+1)
            bfs(root.right,level+1)
        bfs(root,0)
        return list(arr.values())