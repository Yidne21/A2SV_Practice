# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            _sum = n1 + n2 + carry
            carry = _sum // 10
            _sum = _sum % 10

            cur.next = ListNode(_sum)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
