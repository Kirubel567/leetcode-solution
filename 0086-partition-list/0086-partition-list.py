# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            
        smaller = ListNode(0)
        greater = ListNode(0) 

        ptrSmaller = smaller 
        ptrGreater = greater

        while head: 
            if head.val < x: 
                ptrSmaller.next = head
                ptrSmaller = ptrSmaller.next
            else: 
                ptrGreater.next = head
                ptrGreater = ptrGreater.next
            head = head.next
        #now just connect the two halves using the smaller.next = greater
        ptrGreater.next = None
        ptrSmaller.next = greater.next

        return smaller.next

