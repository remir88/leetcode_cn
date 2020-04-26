#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoLists(self, l1: ListNode, l2: ListNode, l: ListNode) -> bool:
        p = False
        if (l1.next != None):
            p = self.addTwoLists(l1.next, l2.next, l)
        t = ListNode(l1.val + l2.val)
        if (p):
            t.val += 1
        p = False
        if (t.val > 10):
            t.val -= 10
            p = True            
        l.next = t
        return p

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        if (self.addTwoLists(l1, l2, l)):
            t = ListNode(1)
            t.next = l
            return t
        else:
            return l

# @lc code=end

