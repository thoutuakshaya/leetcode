# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key <root.val:
            self.deleteNode(root.left,key)
        elif key>root.val:
            self.deleteNode(root.right,key)
        else:
            #key found annat
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                #both present 
                temp=root.right
                while temp.left :
                    temp=temp.left
                root.val=temp.val
                root.right=self.deleteNode(root.right,temp.val)
        return root