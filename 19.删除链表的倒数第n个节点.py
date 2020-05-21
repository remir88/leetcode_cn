#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        
        if length==n:
            return head.next

        p = head
        for i in range(1, length-n):
            p = p.next

        p.next = p.next.next
        return head

# @lc code=end

