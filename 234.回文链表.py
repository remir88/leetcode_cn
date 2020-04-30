#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        cur = prev = None
        while head:
            cur = ListNode(head.val)
            cur.next = prev
            prev = cur
            head = head.next
        return cur
    
    def llen(self, head:ListNode) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l

    def isPalindrome(self, head: ListNode) -> bool:
        rev = self.reverse(head)
        l1 = self.llen(head)
        l2 = self.llen(rev)
        if l1!=l2:
            return False
        for x in range(0, l1//2):
            if (head.val != rev.val):
                return False
            head = head.next
            rev = rev.next
        return True

# @lc code=end

