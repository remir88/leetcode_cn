# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def invertTree(self, root):
		if (root == None):
			return None
		inverted = TreeNode(root.val)
		inverted.left = self.invertTree(root.right)
		inverted.right = self.invertTree(root.left)
		return inverted
	