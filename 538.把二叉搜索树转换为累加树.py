#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    __traverse = []
    __sum = []
    def __init__(self):
        self.__traverse = []
        self.__sum = []
    
    def preorder(self, root: TreeNode):
        if root==None:
            return
        self.__traverse.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def sumb(self, val: int) -> int:
        s = 0
        for i in range(len(self.__traverse)-1, -1, -1):        
            if self.__traverse[i]>val:
                s = s+self.__sum[i]
                break
        return s

    def add(self, root: TreeNode):
        if root==None:
            return
        root.val += self.sumb(root.val)
        self.add(root.left)
        self.add(root.right)

    def gensum(self):
        if self.__traverse==[]:
            return
        self.__sum.append(self.__traverse[0])
        for i in range(1, len(self.__traverse)):
            self.__sum.append(self.__sum[i-1] + self.__traverse[i])

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.preorder(root)
        self.__traverse.sort(reverse=True)
        self.gensum()
        self.add(root)
        return root

# @lc code=end

