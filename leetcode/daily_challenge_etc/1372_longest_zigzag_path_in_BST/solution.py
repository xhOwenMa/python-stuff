# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        # create this to keep track of the longest path length
        self.pathLength = 0

        def search(node, dir: bool, counts: int):
            """
            dir : True means to go left; False means to go right
            """

            if node:
                self.pathLength = max(self.pathLength, counts)
                if dir:
                    search(node.left, False, counts + 1)
                    search(node.right, True, 1)
                else:
                    search(node.left, False, 1)
                    search(node.right, True, counts + 1)

        search(root, False, 0) # initially, the direction does not matter
        return self.pathLength