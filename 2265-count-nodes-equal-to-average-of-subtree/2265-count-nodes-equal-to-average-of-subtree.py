# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=0
        def find(root):
            nonlocal count
            if not root :
                return 0,0

            ls,lc=find(root.left)
            rs,rc=find(root.right)
            s=root.val+ls+rs
            c=1+lc+rc
            avg=s//c
            if avg==root.val:
                count+=1
            return s,c
        find(root)
        return count