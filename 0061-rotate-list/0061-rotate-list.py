# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #use two pointer, this seems like remove nth node from the end of the list 
        #move the second  ptr k+1 times then move the second pointer until first points outside 
        dummy = ListNode(0, head)
        slow = fast = dummy 
        
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        if not head: 
            return None 
        k = k % length
        for _ in range(k+1): 
            fast = fast.next
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next 
        
        slow = slow.next

        fast.next = head
        head = slow.next 
        slow.next = None 

        return head