#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None and l2 == None):
            return None
        prev = head = ListNode(0)
        head.next = prev
        while (l1 != None or l2 != None):
            if (l1 == None):
                current = ListNode(l2.val)
                prev.next = current
                prev = current
                l2 = l2.next               
                continue
            if (l2 == None):
                current = ListNode(l1.val)
                prev.next = current
                prev = current
                l1 = l1.next
                continue
            if (l1.val < l2.val):
                current = ListNode(l1.val)
                l1 = l1.next
            else:
                current = ListNode(l2.val)
                l2 = l2.next
            prev.next = current
            prev = current
        return head.next
# @lc code=end

