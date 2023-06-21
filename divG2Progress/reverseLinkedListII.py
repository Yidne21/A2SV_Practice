# Python implementation of the reverseBetween function for a singly-linked list.

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        Reverses a linked list between two specified positions.

        Args:
        head (ListNode): The head of the linked list.
        left (int): The starting position of the sublist to be reversed.
        right (int): The ending position of the sublist to be reversed.

        Returns:
        ListNode: The head of the reversed linked list.

        """
        current = head
        prev = None
        cnt = 1

        while current:
            if cnt == left:
                break
            prev = current
            current = current.next
            cnt += 1

        leftNode = current
        beforeLeftNode = prev

        while current and cnt <= right:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            cnt += 1
            
        if beforeLeftNode:
            beforeLeftNode.next = prev
        else:
            head = prev

        leftNode.next = current

        return head
