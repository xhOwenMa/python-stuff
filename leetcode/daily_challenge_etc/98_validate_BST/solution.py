# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        will use a recursive helper function        
        """

        def validate(node, low = -math.inf, high = math.inf):
            """
            keep the low and high limit as we traverse the tree and compare node's value with these limits
            return True if the tree is a valid BST; False otherwise
            """

            if not node:
                return True

            # current node's value must be between low and high limits
            if node.val <= low or node.val >= high:
                return False

            # left and right subtree of the current node must also be valid
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))


        return validate(root)    
        