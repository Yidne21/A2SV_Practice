# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy
        cond = float('inf')

        while list1 or list2:
            n1 = list1.val if list1 else cond
            n2 = list2.val if list2 else cond

            if n1 < n2:
                cur.next = ListNode(n1)
                list1 = list1.next
            elif n2 < n1:
                cur.next = ListNode(n2)
                list2 = list2.next
            else:
                cur.next = ListNode(n1)
                cur = cur.next
                cur.next = ListNode(n2)
                list1 = list1.next
                list2 = list2.next
            
            cur = cur.next
        
        return dummy.next
