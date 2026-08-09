class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Key not found
        if root is None:
            return None

        # Search left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Found the node
        else:

            # Case 1: no left child
            if root.left is None:
                return root.right

            # Case 2: no right child
            if root.right is None:
                return root.left

            # Case 3: both children exist
            # Find smallest node in right subtree
            temp = root.right

            while temp.left:
                temp = temp.left

            # Replace current value
            root.val = temp.val

            # Delete duplicate node
            root.right = self.deleteNode(root.right, temp.val)

        return root