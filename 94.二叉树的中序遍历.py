#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root:
            ans += self.inorderTraversal(root.left)
            ans.append(root.val)
            ans += self.inorderTraversal(root.right)
        return ans

# @lc code=end

