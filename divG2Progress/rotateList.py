class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        
        if k == 0:
            return head
        
        startHead = length - k - 1
        newTail = head
        for _ in range(startHead):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        tail.next = head
        
        return newHead
