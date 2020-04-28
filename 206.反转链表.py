#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        prev = None
        while head:
            cur = ListNode(head.val)
            cur.next = prev
            prev = cur
            head = head.next
        return prev      

# @lc code=end

