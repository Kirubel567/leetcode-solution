# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #find the middle element
        right = self.middle(head)
        #split the list
        left = head
        temp = right.next #the second half
        right.next = None

        #repeat this recursively
        left = self.sortList(left)
        right = self.sortList(temp)

        return self.merged(left, right)
    
    def middle(self, head): 
        left = head
        right = head.next

        while right and right.next: 
            left = left.next
            right = right.next.next
        
        return left

    def merged(self, left, right): 
        tail = dummy = ListNode()

        while left and right: 
            if left.val < right.val: 
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left: 
            tail.next = left
        if right: 
            tail.next = right
        
        return dummy.next
    
    


