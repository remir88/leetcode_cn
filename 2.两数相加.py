#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = None
        plus = 0
        while ((l1 != None) or (l2 != None)):
            v1 = v2 = 0
            if (l1 != None):
                v1 = l1.val
            if (l2 != None):
                v2 = l2.val
            current = ListNode(v1 + v2 + plus)
            if (prev != None):
                prev.next = current
            else:
                head = current
            if (current.val >= 10):
                current.val -= 10
                plus = 1
            else:
                plus = 0
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
            prev = current

        if (plus == 1):
            current = ListNode(1)
            prev.next = current

        return head
        
# @lc code=end

