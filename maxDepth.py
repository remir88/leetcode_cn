# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxd = 1
    def maxDepth(self, root, depth=1):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        if (depth>self.maxd):
            self.maxd = depth
        if (root.left != None):
            self.maxDepth(root.left, depth+1)
        if (root.right != None):
            self.maxDepth(root.right, depth+1)
        return self.maxd
        
