# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # variable to keep track the maximum width
        self.max_width = 0

        # use Python dequeue to implement BFS
        dq = deque()
        dq.append([root, 0]) # insert (node, index) pair into queue
        
        while dq:
            n = len(dq)

            # create a list to store the indices of the nodes at this level
            indices = []

            for _ in range(n):
                node, index = dq.popleft() # we want to traverse the level from left to right
                indices.append(index)

                if node.left:
                    dq.append([node.left, 2*index+1])
                if node.right:
                    dq.append([node.right, 2*index+2])

            # indices[-1] would be the right-most node at this level
            # indices[0] is the left-most node at this level
            self.max_width = max(self.max_width, indices[-1] - indices[0] + 1)

        return self.max_width

