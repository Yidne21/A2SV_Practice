# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        slow = fast = head.next

        while fast.next:
            fast = fast.next

            if fast.next:
                slow = slow.next
                fast = fast.next
        
        return slow
